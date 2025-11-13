import subprocess
import os
import time
import pandas as pd
import glob
from typing import Dict, List, Union, Tuple, Optional
import re
import shutil
import mph  # COMSOL Python API

# 批量梯度下降 (Batch Gradient Descent - BGD), 中心差分
class COMSOLOptimization:
    def __init__(self, model_path: str, results_dir: str, 
                 result_expressions: List[str], standard_values: Dict[str, float], 
                 weights: Dict[str, float], max_iter: int = 100, 
                 perturbation: Union[float, Dict[str, float]] = 0.01, 
                 threshold: float = 0.001, learning_rate: float = 0.05):
        # COMSOL 模型配置
        self.model_path = model_path
        self.results_dir = results_dir
        os.makedirs(results_dir, exist_ok=True)
        
        # 参数配置
        self.result_expressions = result_expressions
        self.standard_values = standard_values
        self.weights = weights
        
        # 优化参数
        self.max_iter = max_iter
        self.perturbation = perturbation
        self.threshold = threshold
        self.learning_rate = learning_rate
        
        # 状态变量
        self.current_error = float('inf')
        self.current_keyvalues: List[float] = []
        self.parameters: List[Dict] = []
        self.param_perturbations: List[float] = []
        
        # 初始化 COMSOL 客户端和模型
        self.client = mph.start()
        self.model = self.client.load(model_path)
        print(f"已加载 COMSOL 模型: {model_path}")
        
        # 初始化参数
        self._parse_model_parameters()

    def run_simulation(self) -> bool:
        """运行 COMSOL 仿真"""
        try:
            start_time = time.time()
            self.model.solve()
            run_time = time.time() - start_time
            print(f"仿真完成! 运行时间: {run_time:.2f} 秒")
            return True
        except Exception as e:
            print(f"COMSOL 仿真失败: {str(e)}")
            return False

    def _extract_results(self) -> Dict[str, float]:
        """从 COMSOL 模型中提取结果"""
        results = {}
        for expr in self.result_expressions:
            try:
                # 计算表达式结果
                value = self.model.evaluate(expr)
                # 如果是数组，取最后一个值
                if isinstance(value, list):
                    value = value[-1]
                results[expr] = float(value)
            except Exception as e:
                print(f"无法提取表达式 '{expr}' 的结果: {str(e)}")
                results[expr] = 0.0
        return results

    def _calculate_total_simulation_error(
        self,
        actual_values: Dict[str, float],
        output_file: Optional[str] = None
        ) -> Tuple[float, Dict[str, float], Dict[str, float]]:
        """计算仿真总误差"""
        absolute_errors = {}
        weighted_errors = {}
        total_error = 0.0

        for expr, actual in actual_values.items():
            standard = self.standard_values.get(expr, 0.0)
            weight = self.weights.get(expr, 1.0)
            
            abs_error = abs(actual - standard)
            absolute_errors[expr] = abs_error
            
            weighted_error = abs_error * weight
            weighted_errors[expr] = weighted_error
            
            total_error += weighted_error

        # 输出结果
        print("\n误差分析结果:")
        print(f"{'表达式':<30} {'实际值':>10} {'标准值':>10} {'绝对误差':>12} {'权重':>8} {'加权误差':>12}")
        print("-" * 90)
        for expr in absolute_errors.keys():
            print(f"{expr:<30} {actual_values[expr]:>10.4f} {self.standard_values.get(expr, 0.0):>10.4f} "
                f"{absolute_errors[expr]:>12.4f} {self.weights.get(expr, 1.0):>8.2f} "
                f"{weighted_errors[expr]:>12.4f}")
        print("-" * 90)
        print(f"总仿真误差: {total_error:.4f}")

        # 保存结果到文件
        if output_file:
            results_df = pd.DataFrame({
                'Expression': list(absolute_errors.keys()),
                'Actual_Value': [actual_values[expr] for expr in absolute_errors.keys()],
                'Standard_Value': [self.standard_values.get(expr, 0.0) for expr in absolute_errors.keys()],
                'Absolute_Error': [absolute_errors[expr] for expr in absolute_errors.keys()],
                'Weight': [self.weights.get(expr, 1.0) for expr in absolute_errors.keys()],
                'Weighted_Error': [weighted_errors[expr] for expr in absolute_errors.keys()]
            })
            results_df.loc['Total'] = ['-', '-', '-', '-', '-', total_error]
            results_df.to_csv(output_file, index=False)
            print(f"结果已保存到: {output_file}")
        
        return total_error, absolute_errors, weighted_errors

    def _parse_model_parameters(self) -> None:
        """从描述字段中提取优化元数据"""
        # 获取模型中所有参数及其描述
        all_params = self.model.parameters()
        
        parameters = []
        for param_name in all_params:
            try:
                # 获取参数描述
                description = self.model.description(param_name)
                
                # 检查是否有优化元数据
                if description and description.startswith('[') and description.endswith(']'):
                    print(f"发现优化参数: {param_name} - {description}")
                    
                    # 提取元数据
                    meta_str = description[1:-1]
                    meta_dict = {}
                    for item in meta_str.split(','):
                        key, value = item.split(':')
                        meta_dict[key.strip()] = float(value.strip())
                    
                    # 获取当前值
                    current_value = float(self.model.parameter(param_name))
                    
                    # 添加到参数列表
                    parameters.append({
                        'name': param_name,
                        'value': current_value,
                        'min': meta_dict.get('min', 0),
                        'max': meta_dict.get('max', 1),
                        'perturb': meta_dict.get('perturb', self.perturbation)
                    })
            except Exception as e:
                print(f"处理参数 '{param_name}' 时出错: {str(e)}")
        if not parameters:
            print("警告: 未找到任何可优化参数")
        else:
            print(f"找到 {len(parameters)} 个可优化参数")
        
        self.parameters = parameters
        self.current_keyvalues = [p['value'] for p in parameters]
        self.param_perturbations = [p['perturb'] for p in parameters]

    @staticmethod
    def _clip_value(value: float, min_val: float, max_val: float) -> float:
        """确保参数值在指定范围内"""
        return max(min_val, min(value, max_val))

    def _update_parameters(self, new_values: List[float]) -> None:
        """更新 COMSOL 模型参数"""
        print("\n更新模型参数...")
        for param, new_value in zip(self.parameters, new_values):
            # 确保新值在合理范围内
            clipped_value = self._clip_value(new_value, param['min'], param['max'])
            
            # 更新模型参数
            self.model.parameter(param['name'], str(clipped_value))
            print(f"参数 '{param['name']}': {param['value']:.6f} -> {clipped_value:.6f} " 
                  f"(范围: [{param['min']}, {param['max']}])")
            
            # 更新当前值记录
            param['value'] = clipped_value

    def compute_error(self) -> float:
        """运行仿真并计算误差"""
        # 运行仿真
        success = self.run_simulation()
        if not success:
            raise RuntimeError("COMSOL 仿真运行失败")
        
        # 提取结果
        actual_values = self._extract_results()
        
        # 计算误差
        total_error, _, _ = self._calculate_total_simulation_error(
            actual_values,
            output_file=os.path.join(self.results_dir, f"error_analysis_{time.strftime('%Y%m%d_%H%M%S')}.csv")
        )
        
        return total_error

    def optimize(self) -> None:
        """执行参数优化主循环"""
        print("\n" + "="*50)
        print("开始优化过程")
        print("="*50)
        
        # 初始误差计算
        self.current_error = self.compute_error()
        print(f"\n初始误差: {self.current_error:.6f}")
        
        # 保存初始模型状态
        initial_model_path = os.path.join(self.results_dir, "initial_model.mph")
        self.model.save(initial_model_path)
        print(f"初始模型已保存到: {initial_model_path}")
        
        # 梯度下降优化
        for iteration in range(1, self.max_iter + 1):
            print("\n" + "="*50)
            print(f"迭代 {iteration}/{self.max_iter}")
            print("="*50)
            
            gradients = []

            # 使用中心差分法计算梯度
            for i, param in enumerate(self.parameters):
                print(f"\n计算参数 '{param['name']}' 的梯度...")
                perturb = self.param_perturbations[i]
                orig_value = param['value']
                
                # 正向扰动
                self.model.parameter(param['name'], str(orig_value + perturb))
                error_plus = self.compute_error()
                
                # 负向扰动
                self.model.parameter(param['name'], str(orig_value - perturb))
                error_minus = self.compute_error()
                
                # 恢复原始值
                self.model.parameter(param['name'], str(orig_value))
                
                # 中心差分梯度
                gradient = (error_plus - error_minus) / (2 * perturb)
                gradients.append(gradient)
                print(f"梯度: {gradient:.6f} (正向误差: {error_plus:.6f}, 负向误差: {error_minus:.6f})")
            
            # 更新参数：θ = θ - η * ∇θ
            new_values = []
            for i, param in enumerate(self.parameters):
                param_range = param['max'] - param['min']
                scaled_lr = self.learning_rate * param_range
                
                new_val = param['value'] - scaled_lr * gradients[i]
                new_val = self._clip_value(new_val, param['min'], param['max'])
                new_values.append(new_val)
            
            # 应用新参数
            self._update_parameters(new_values)
            self.current_keyvalues = new_values
            
            # 计算新误差
            new_error = self.compute_error()
            
            # 检查收敛
            error_reduction = abs(self.current_error - new_error)
            print(f"\n迭代 {iteration} 结果: "
                  f"前误差={self.current_error:.6f}, 新误差={new_error:.6f}, "
                  f"误差变化={error_reduction:.6f}")
            
            self.current_error = new_error
            
            # 检查是否满足停止条件
            if self.current_error < self.threshold:
                print(f"\n优化收敛! 误差变化 ({error_reduction:.6f}) 小于阈值 ({self.threshold})")
                break
        
        # 输出最终结果
        print("\n" + "="*50)
        print("优化完成!")
        print("="*50)
        print(f"最终误差: {self.current_error:.6f}")
        print("\n优化后的参数值:")
        for i, param in enumerate(self.parameters):
            print(f"{param['name']}: {self.current_keyvalues[i]}")
        
        # 保存最终模型
        final_model_path = os.path.join(self.results_dir, "optimized_model.mph")
        self.model.save(final_model_path)
        print(f"\n优化后的模型已保存到: {final_model_path}")


def main():
    # 配置参数
    config = {
        "model_path": "D:\\Python\\第二版平推流（活化能调整）.mph",
        "results_dir": "D:\\Python\\result",
        "result_expressions": [
            "NO_con",  
            "CO_con",  
            "C3H6_con"
        ],
        "standard_values": {
            "NO_con": 300.0,
            "CO_con": 350.0,
            "C3H6_con": 400.0
        },
        "weights": {
            "NO_con": 1.0,
            "CO_con": 0.8,
            "C3H6_con": 1.5
        },
        "max_iter": 50,
        "perturbation": 0.1,
        "threshold": 0.01,
        "learning_rate": 0.1
    }
    
    # 创建优化仿真对象
    optimizer = COMSOLOptimization(**config)
    
    # 执行优化
    optimizer.optimize()

if __name__ == "__main__":
    main()