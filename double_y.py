import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from scipy.interpolate import make_interp_spline
import pandas as pd
from matplotlib.lines import Line2D

plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 12,         # 图例字号
            'xtick.labelsize': 12,         # X轴刻度字号
            'ytick.labelsize': 12,         # Y轴刻度字号
            'xtick.major.width': 1.2,      # X轴主刻度线宽
            'ytick.major.width': 1.2,      # Y轴主刻度线宽
            'xtick.major.size': 5,         # X轴主刻度长度
            'ytick.major.size': 5,         # Y轴主刻度长度
            'xtick.direction': 'in',       # X刻度方向向内
            'ytick.direction': 'in',       # Y刻度方向向内
            'figure.dpi': 300,             # 输出分辨率
            'savefig.dpi': 300,            # 保存图像分辨率
            'savefig.bbox': 'tight',       # 保存时裁剪空白
            'savefig.pad_inches': 0.1      # 保存时内边距
        })

# 创建示例数据
data = pd.read_csv('I:\home\huyu\RETA\ML\HTTF_SAMall_steady9.csv')
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

y1 = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13]
y2 = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]

x = np.array([0.1089,0.1928,0.2201,0.2462,0.2757,0.3040,0.3324,0.3585,0.3891,0.4152,0.4413,0.4708,0.5525])
y1_ref = [0.027,0.024,0.042,0.079,0.092,0.092,0.104,0.117,0.112,0.119,0.066,0.039,0.096]    
y2_ref = [564,951,976,955,960,963,964,965,963,951,981,958,625]

# 创建光滑曲线（使用样条插值）
x_smooth = np.linspace(x.min(), x.max(), 300)  # 300个点用于光滑曲线

# 为y1创建光滑曲线
spl1 = make_interp_spline(x, y1, k=1)  # 三次样条插值
y1_smooth = spl1(x_smooth)

spl1_ref = make_interp_spline(x, y1_ref, k=1)  # 三次样条插值
y1_ref_smooth = spl1_ref(x_smooth)

# 为y2创建光滑曲线
spl2 = make_interp_spline(x, y2, k=1)  # 三次样条插值
y2_smooth = spl2(x_smooth)

spl2_ref = make_interp_spline(x, y2_ref, k=1)  # 三次样条插值
y2_ref_smooth = spl2_ref(x_smooth)

# 创建图形和第一个Y轴
fig, ax1 = plt.subplots(figsize=(5, 10))

# 绘制第一个数据集的光滑曲线（左侧Y轴）
ax1.plot(x_smooth, y1_smooth, 'blue', linewidth=2, label='Flow rate')
ax1.plot(x_smooth, y1_ref_smooth, 'blue', linewidth=1, linestyle='--', label='Flow rate_SAM')

# 标记第一个数据集的原始数据点
ax1.scatter(x, y1, color='blue', s=60, zorder=5, edgecolor='black', 
             alpha=0.8)
ax1.scatter(x, y1_ref, color='green', s=60, zorder=5, edgecolor='black', 
             alpha=0.8, marker='o') 

# 设置第一个Y轴标签和颜色
ax1.set_xlabel('Radial coordinate(m)')
ax1.set_ylabel('Flow rate(kg/s)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# 设置第一个Y轴的范围和刻度间隔
ax1.set_ylim(0, 0.14)  # Y1轴范围
ax1.yaxis.set_major_locator(MultipleLocator(0.01))  # Y1轴主刻度间隔
ax1.yaxis.set_minor_locator(MultipleLocator(0.005))  # Y1轴次刻度间隔

# 创建第二个Y轴（共享X轴）
ax2 = ax1.twinx()

# 绘制第二个数据集的光滑曲线（右侧Y轴）
ax2.plot(x_smooth, y2_smooth, 'red', linewidth=2, label='Temperature')
ax2.plot(x_smooth, y2_ref_smooth,'red', linewidth=1, linestyle='--', label='Temperature_SAM')

# 标记第二个数据集的原始数据点
ax2.scatter(x, y2, color='red', s=60, zorder=5, edgecolor='black', 
            alpha=0.8)
ax2.scatter(x, y2_ref, color='orange', s=60, zorder=5, edgecolor='black', 
            alpha=0.8, marker='o')

# 设置第二个Y轴标签和颜色
ax2.set_ylabel('Temperature(K)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# 设置第二个Y轴的范围和刻度间隔
ax2.set_ylim(0, 1100)  # Y2轴范围
ax2.yaxis.set_major_locator(MultipleLocator(200))  # Y2轴主刻度间隔
ax2.yaxis.set_minor_locator(MultipleLocator(50))  # Y2轴次刻度间隔

# 添加网格线
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.grid(True, which='minor', linestyle=':', alpha=0.4)

# 添加图例
# 合并两个轴的图例
# 创建自定义图例句柄，模仿您图中的样式
legend_handles = [
    # 流量 - 实际数据
    Line2D([0], [0], color='blue', linewidth=2, 
           marker='o', markersize=4, markerfacecolor='blue',
           markeredgecolor='black', label='Flow rate-RETA'),
    # 流量 - 参考数据
    Line2D([0], [0], color='blue', linewidth=1, linestyle='--',
           marker='o', markersize=4, markerfacecolor='green',
           markeredgecolor='black', label='Flow rate-SAM'),
    # 温度 - 实际数据
    Line2D([0], [0], color='red', linewidth=2,
           marker='o', markersize=4, markerfacecolor='red',
           markeredgecolor='black', label='Temperature-RETA'),
    # 温度 - 参考数据
    Line2D([0], [0], color='red', linewidth=1, linestyle='--',
           marker='o', markersize=4, markerfacecolor='orange',
           markeredgecolor='black', label='Temperature-SAM')
]

# 使用自定义图例
ax1.legend(handles=legend_handles, loc='lower center',
           frameon=True, framealpha=0.9, shadow=True,
           borderpad=1.2, handlelength=2.0,fontsize=7)

# 添加标题
plt.title('Temperature and flow rate comparison of steady state', fontsize=14, pad=20)

# 优化布局
#fig.tight_layout()

# 显示图形
plt.show()