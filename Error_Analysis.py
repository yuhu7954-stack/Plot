import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

# 设置学术论文级别的样式
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'mathtext.fontset': 'stix',
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'legend.fontsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'figure.autolayout': False,
    'axes.linewidth': 0.8,
    'grid.linewidth': 0.5,
    'lines.linewidth': 1.2,
    'patch.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8
})

# 示例数据 - 请替换为您的实际数据
channels = [f'Channel {i+1}' for i in range(13)]

# 创建示例数据
data = pd.read_csv('D:\Python\HTTF稳态结果\HTTF_SAMall_steady9.csv')
a1 = data.iloc[2]["cooled_center_low:outlet:mass"]
a2 = data.iloc[2]["cooled_1_low:outlet:mass"]
a3 = data.iloc[2]["cooled_2_low:outlet:mass"]
a4 = data.iloc[2]["cooled_3_low:outlet:mass"]
a5 = data.iloc[2]["cooled_4_low:outlet:mass"]
a6 = data.iloc[2]["cooled_5_low:outlet:mass"]
a7 = data.iloc[2]["cooled_6_low:outlet:mass"]
a8 = data.iloc[2]["cooled_7_low:outlet:mass"]
a9 = data.iloc[2]["cooled_8_low:outlet:mass"]
a10 = data.iloc[2]["cooled_9_low:outlet:mass"]
a11 = data.iloc[2]["cooled_10_low:outlet:mass"]
a12 = data.iloc[2]["cooled_11_low:outlet:mass"]
a13 = data.iloc[2]["cooled_side_low:outlet:mass"]

b1 = data.iloc[2]["cooled_center_low:T_out"]
b2 = data.iloc[2]["cooled_1_low:T_out"]
b3 = data.iloc[2]["cooled_2_low:T_out"]
b4 = data.iloc[2]["cooled_3_low:T_out"]
b5 = data.iloc[2]["cooled_4_low:T_out"]
b6 = data.iloc[2]["cooled_5_low:T_out"]
b7 = data.iloc[2]["cooled_6_low:T_out"]
b8 = data.iloc[2]["cooled_7_low:T_out"]
b9 = data.iloc[2]["cooled_8_low:T_out"]
b10 = data.iloc[2]["cooled_9_low:T_out"]
b11 = data.iloc[2]["cooled_10_low:T_out"]
b12 = data.iloc[2]["cooled_11_low:T_out"]
b13 = data.iloc[2]["cooled_side_low:T_out"]

# x = np.array([0.1089,0.1928,0.2201,0.2462,0.2757,0.3040,0.3324,0.3585,0.3891,0.4152,0.4413,0.4708,0.5525])
# y1_ref = [0.027,0.024,0.042,0.079,0.092,0.092,0.104,0.117,0.112,0.119,0.066,0.039,0.096]    
# y2_ref = [564,951,976,955,960,963,964,965,963,951,981,958,625]

# 冷却剂质量流量数据 (kg/s)
sim_flow = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13]
ref_flow = [0.027,0.024,0.042,0.079,0.092,0.092,0.104,0.117,0.112,0.119,0.066,0.039,0.096]

# 出口温度数据 (K)
sim_temp = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]
ref_temp = [564,951,976,955,960,963,964,965,963,951,981,958,625]

def calculate_errors(sim, ref):
    """计算绝对误差和相对误差"""
    abs_errors = [s - r for s, r in zip(sim, ref)]
    rel_errors = [(s - r) / r * 100 if r != 0 else 0 for s, r in zip(sim, ref)]
    return abs_errors, rel_errors

# 计算误差
flow_abs_errors, flow_rel_errors = calculate_errors(sim_flow, ref_flow)
temp_abs_errors, temp_rel_errors = calculate_errors(sim_temp, ref_temp)

# 设置条形图的y轴位置
y = np.arange(len(channels))
height = 0.35  # 条形的高度

# 定义学术风格的颜色
colors = {
    'simulation': '#2E86AB',  # 深蓝色
    'reference': '#A23B72',   # 深紫色
    'error_pos': '#F18F01',   # 橙色
    'error_neg': '#C73E1D',   # 红色
    'grid': '#D8D8D8',        # 浅灰色
    'text': '#2B2D42'         # 深灰色
}

# 1. 生成流量对比图
fig1, ax1 = plt.subplots(figsize=(8, 6))

# 绘制条形图
bars1 = ax1.barh(y - height/2, sim_flow, height, 
                label='Simulation', color=colors['simulation'], alpha=0.9, edgecolor='white', linewidth=0.5)
bars2 = ax1.barh(y + height/2, ref_flow, height, 
                label='Reference', color=colors['reference'], alpha=0.9, edgecolor='white', linewidth=0.5)

# 添加连接线显示差异
for i, (s, r) in enumerate(zip(sim_flow, ref_flow)):
    y_pos = y[i]
    ax1.plot([min(s, r), max(s, r)], [y_pos, y_pos], 
             color='gray', linewidth=0.8, alpha=0.7, linestyle='--')

# 添加误差标注
for i, (abs_err, rel_err) in enumerate(zip(flow_abs_errors, flow_rel_errors)):
    width = max(sim_flow[i], ref_flow[i])
    error_color = colors['error_pos'] if abs_err >= 0 else colors['error_neg']
    
    ax1.text(width + 0.03, y[i], 
             f'{abs_err:+.3f} kg/s\n({rel_err:+.1f}%)', 
             ha='left', va='center', fontsize=8, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", 
                      edgecolor=error_color, alpha=0.9, linewidth=0.8))

ax1.set_ylabel('Cooling Channels', fontweight='bold')
ax1.set_xlabel('Mass Flow Rate (kg/s)', fontweight='bold')
ax1.set_title('Comparison of Coolant Mass Flow Rates:\nSimulation vs Reference Results', 
              fontsize=12, fontweight='bold', pad=15)
ax1.set_yticks(y)
ax1.set_yticklabels(channels)
ax1.legend(loc='lower right', frameon=True, fancybox=False, edgecolor='black', framealpha=0.9)
ax1.grid(True, alpha=0.4, axis='x', color=colors['grid'])
ax1.set_axisbelow(True)  # 将网格线放在数据后面

# 设置x轴格式
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# 添加统计信息框
flow_mae = np.mean(np.abs(flow_abs_errors))
flow_rmse = np.sqrt(np.mean(np.array(flow_abs_errors)**2))
max_flow_error = max(np.abs(flow_abs_errors))

stats_text = f'MAE: {flow_mae:.4f} kg/s\nRMSE: {flow_rmse:.4f} kg/s\nMax Error: {max_flow_error:.4f} kg/s'
ax1.text(0.02, 0.98, stats_text, transform=ax1.transAxes, fontsize=9,
         verticalalignment='top', bbox=dict(boxstyle="round", facecolor="white", 
                                           edgecolor=colors['simulation'], alpha=0.9))

# 调整布局
fig1.tight_layout()

# 保存图片
plt.savefig('mass_flow_comparison.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('mass_flow_comparison.pdf', bbox_inches='tight', 
            facecolor='white', edgecolor='none')

# 显示图表
plt.show()

# 2. 生成温度对比图
fig2, ax2 = plt.subplots(figsize=(8, 6))

# 绘制条形图
bars3 = ax2.barh(y - height/2, sim_temp, height, 
                label='Simulation', color=colors['simulation'], alpha=0.9, edgecolor='white', linewidth=0.5)
bars4 = ax2.barh(y + height/2, ref_temp, height, 
                label='Reference', color=colors['reference'], alpha=0.9, edgecolor='white', linewidth=0.5)

# 添加连接线显示差异
for i, (s, r) in enumerate(zip(sim_temp, ref_temp)):
    y_pos = y[i]
    ax2.plot([min(s, r), max(s, r)], [y_pos, y_pos], 
             color='gray', linewidth=0.8, alpha=0.7, linestyle='--')

# 添加误差标注
for i, (abs_err, rel_err) in enumerate(zip(temp_abs_errors, temp_rel_errors)):
    width = max(sim_temp[i], ref_temp[i])
    error_color = colors['error_pos'] if abs_err >= 0 else colors['error_neg']
    
    ax2.text(width + 0.5, y[i], 
             f'{abs_err:+.1f} K\n({rel_err:+.2f}%)', 
             ha='left', va='center', fontsize=8, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", 
                      edgecolor=error_color, alpha=0.9, linewidth=0.8))

ax2.set_ylabel('Cooling Channels', fontweight='bold')
ax2.set_xlabel('Outlet Temperature (K)', fontweight='bold')
ax2.set_title('Comparison of Coolant Outlet Temperatures:\nSimulation vs Reference Results', 
              fontsize=12, fontweight='bold', pad=15)
ax2.set_yticks(y)
ax2.set_yticklabels(channels)
ax2.legend(loc='lower right', frameon=True, fancybox=False, edgecolor='black', framealpha=0.9)
ax2.grid(True, alpha=0.4, axis='x', color=colors['grid'])
ax2.set_axisbelow(True)  # 将网格线放在数据后面

# 设置x轴格式
ax2.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

# 添加统计信息框
temp_mae = np.mean(np.abs(temp_abs_errors))
temp_rmse = np.sqrt(np.mean(np.array(temp_abs_errors)**2))
max_temp_error = max(np.abs(temp_abs_errors))

stats_text = f'MAE: {temp_mae:.2f} K\nRMSE: {temp_rmse:.2f} K\nMax Error: {max_temp_error:.2f} K'
ax2.text(0.02, 0.98, stats_text, transform=ax2.transAxes, fontsize=9,
         verticalalignment='top', bbox=dict(boxstyle="round", facecolor="white", 
                                           edgecolor=colors['simulation'], alpha=0.9))

# 调整布局
fig2.tight_layout()

# 保存图片
plt.savefig('temperature_comparison.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('temperature_comparison.pdf', bbox_inches='tight', 
            facecolor='white', edgecolor='none')

# 显示图表
plt.show()

# 打印详细误差表格
print("\nDetailed Error Analysis:")
print("=" * 85)
print(f"{'Channel':<12} {'Flow Abs Error':<15} {'Flow Rel Error':<15} {'Temp Abs Error':<15} {'Temp Rel Error':<15}")
print("-" * 85)
for i in range(len(channels)):
    print(f"{channels[i]:<12} {flow_abs_errors[i]:+8.4f} kg/s   {flow_rel_errors[i]:+7.2f}%        "
          f"{temp_abs_errors[i]:+7.2f} K        {temp_rel_errors[i]:+7.2f}%")

print("-" * 85)
print(f"{'Average':<12} {np.mean(flow_abs_errors):+8.4f} kg/s   {np.mean(flow_rel_errors):+7.2f}%        "
      f"{np.mean(temp_abs_errors):+7.2f} K        {np.mean(temp_rel_errors):+7.2f}%")
print(f"{'Std Dev':<12} {np.std(flow_abs_errors):8.4f} kg/s   {np.std(flow_rel_errors):7.2f}%        "
      f"{np.std(temp_abs_errors):7.2f} K        {np.std(temp_rel_errors):7.2f}%")