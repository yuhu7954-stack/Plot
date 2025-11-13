import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.patches as patches
import pandas as pd

# 设置学术样式
plt.style.use('seaborn-v0_8-paper')
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'figure.dpi': 300,
    'savefig.dpi': 300,
})

# 数据准备
# 读取数据
data = pd.read_csv('D:\Python\HTTF稳态结果\HTTF_SAMall_steady9.csv')

# 提取质量流量数据
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

# 提取温度数据
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

channels = np.arange(1, 14)
sim_flow = np.array([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13])
ref_flow = np.array([0.027,0.024,0.042,0.079,0.092,0.092,0.104,0.117,0.112,0.119,0.066,0.039,0.096])
sim_temp = np.array([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13])
ref_temp = np.array([564,951,976,955,960,963,964,965,963,951,981,958,625])

# 创建复合图表
fig = plt.figure(figsize=(14, 12))
gs = GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.4)

# 1. 流量散点对比图
ax1 = fig.add_subplot(gs[0, 0])
flow_range = [min(np.min(sim_flow), np.min(ref_flow)) * 0.98, 
              max(np.max(sim_flow), np.max(ref_flow)) * 1.02]

# 绘制完美匹配线
ax1.plot(flow_range, flow_range, 'k--', alpha=0.7, linewidth=1, label='Perfect agreement')

# 绘制数据点
scatter1 = ax1.scatter(ref_flow, sim_flow, c=channels, cmap='viridis', 
                      s=100, alpha=0.8, edgecolors='black', linewidth=0.5)

# 手动设置标注位置 - 更稳定的方法
annotations_positions = {
    1: (1.28, 1.25, 'left', 'top'),
    2: (1.30, 1.32, 'right', 'bottom'),
    3: (1.20, 1.18, 'left', 'top'),
    4: (1.38, 1.41, 'right', 'bottom'),
    5: (1.31, 1.29, 'left', 'top'),
    6: (1.33, 1.35, 'right', 'bottom'),
    7: (1.25, 1.22, 'left', 'top'),
    8: (1.35, 1.38, 'right', 'bottom'),
    9: (1.29, 1.31, 'left', 'top'),
    10: (1.26, 1.27, 'left', 'bottom'),
    11: (1.32, 1.34, 'right', 'top'),
    12: (1.27, 1.26, 'left', 'bottom'),
    13: (1.29, 1.30, 'right', 'top')
}

for i, channel in enumerate(channels):
    x, y = ref_flow[i], sim_flow[i]
    ha, va = annotations_positions[channel][2], annotations_positions[channel][3]
    
    ax1.annotate(f'{channel}', (x, y), 
                xytext=(8 if ha == 'right' else -8, 8 if va == 'top' else -8),
                textcoords='offset points',
                fontsize=9, ha=ha, va=va,
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8, linewidth=0.5),
                arrowprops=dict(arrowstyle='->', color='gray', lw=0.8, alpha=0.7))

ax1.set_xlabel('Reference Mass Flow Rate (kg/s)', fontweight='bold', fontsize=11)
ax1.set_ylabel('RETA Mass Flow Rate (kg/s)', fontweight='bold', fontsize=11)
ax1.set_title('(A) Mass Flow Rate Comparison', fontweight='bold', pad=15, fontsize=12)
ax1.grid(True, alpha=0.3)

# 计算并显示统计信息
flow_r2 = np.corrcoef(ref_flow, sim_flow)[0,1]**2
flow_rmse = np.sqrt(np.mean((sim_flow - ref_flow)**2))
ax1.text(0.05, 0.95, f'$R^2$ = {flow_r2:.4f}\nRMSE = {flow_rmse:.4f} kg/s', 
         transform=ax1.transAxes, 
         bbox=dict(boxstyle="round", facecolor="white", alpha=0.9, edgecolor='gray'),
         verticalalignment='top', fontsize=10)

# 2. 温度散点对比图
ax2 = fig.add_subplot(gs[0, 1])
temp_range = [min(np.min(sim_temp), np.min(ref_temp)) * 0.998, 
              max(np.max(sim_temp), np.max(ref_temp)) * 1.002]

ax2.plot(temp_range, temp_range, 'k--', alpha=0.7, linewidth=1, label='Perfect agreement')

scatter2 = ax2.scatter(ref_temp, sim_temp, c=channels, cmap='viridis', 
                      s=100, alpha=0.8, edgecolors='black', linewidth=0.5)

# 手动设置温度图的标注位置
temp_annotations_positions = {
    1: (344.5, 345.2, 'left', 'top'),
    2: (346.2, 347.8, 'right', 'bottom'),
    3: (342.8, 343.5, 'left', 'top'),
    4: (348.0, 349.1, 'right', 'bottom'),
    5: (345.8, 346.3, 'left', 'top'),
    6: (347.5, 348.2, 'right', 'bottom'),
    7: (343.9, 344.7, 'left', 'top'),
    8: (348.3, 348.9, 'right', 'bottom'),
    9: (346.7, 347.1, 'left', 'top'),
    10: (345.2, 345.8, 'left', 'bottom'),
    11: (347.8, 348.5, 'right', 'top'),
    12: (346.1, 346.6, 'left', 'bottom'),
    13: (346.9, 347.4, 'right', 'top')
}

for i, channel in enumerate(channels):
    x, y = ref_temp[i], sim_temp[i]
    ha, va = temp_annotations_positions[channel][2], temp_annotations_positions[channel][3]
    
    ax2.annotate(f'{channel}', (x, y), 
                xytext=(10 if ha == 'right' else -10, 10 if va == 'top' else -10),
                textcoords='offset points',
                fontsize=9, ha=ha, va=va,
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8, linewidth=0.5),
                arrowprops=dict(arrowstyle='->', color='gray', lw=0.8, alpha=0.7))

ax2.set_xlabel('Reference Outlet Temperature (K)', fontweight='bold', fontsize=11)
ax2.set_ylabel('RETA Outlet Temperature (K)', fontweight='bold', fontsize=11)
ax2.set_title('(B) Outlet Temperature Comparison', fontweight='bold', pad=15, fontsize=12)
ax2.grid(True, alpha=0.3)

temp_r2 = np.corrcoef(ref_temp, sim_temp)[0,1]**2
temp_rmse = np.sqrt(np.mean((sim_temp - ref_temp)**2))
ax2.text(0.05, 0.95, f'$R^2$ = {temp_r2:.4f}\nRMSE = {temp_rmse:.2f} K', 
         transform=ax2.transAxes, 
         bbox=dict(boxstyle="round", facecolor="white", alpha=0.9, edgecolor='gray'),
         verticalalignment='top', fontsize=10)

# 3. Bland-Altman图 (流量)
ax3 = fig.add_subplot(gs[1, 0])
flow_means = (sim_flow + ref_flow) / 2
flow_diffs = sim_flow - ref_flow
flow_mean_diff = np.mean(flow_diffs)
flow_std_diff = np.std(flow_diffs)

# 计算界限
upper_limit = flow_mean_diff + 1.96 * flow_std_diff
lower_limit = flow_mean_diff - 1.96 * flow_std_diff

# 绘制界限线
ax3.axhline(flow_mean_diff, color='red', linestyle='-', alpha=0.8, 
            label=f'Mean: {flow_mean_diff:.4f}')
ax3.axhline(upper_limit, color='red', linestyle='--', alpha=0.6, 
           label=f'+1.96 SD: {upper_limit:.4f}')
ax3.axhline(lower_limit, color='red', linestyle='--', alpha=0.6, 
           label=f'-1.96 SD: {lower_limit:.4f}')

# 填充一致性界限区域
ax3.fill_between([min(flow_means), max(flow_means)], 
                lower_limit, upper_limit, 
                color='red', alpha=0.1)

scatter3 = ax3.scatter(flow_means, flow_diffs, c=channels, cmap='viridis', 
                      s=100, alpha=0.8, edgecolors='black', linewidth=0.5)

# Bland-Altman图的标注位置
ba_flow_positions = {
    1: (1.265, -0.03, 'left', 'top'),
    2: (1.310, 0.02, 'right', 'bottom'),
    3: (1.190, -0.02, 'left', 'top'),
    4: (1.395, 0.03, 'right', 'bottom'),
    5: (1.300, -0.02, 'left', 'top'),
    6: (1.340, 0.02, 'right', 'bottom'),
    7: (1.235, -0.03, 'left', 'top'),
    8: (1.365, 0.03, 'right', 'bottom'),
    9: (1.300, 0.02, 'left', 'top'),
    10: (1.265, 0.01, 'left', 'bottom'),
    11: (1.330, 0.02, 'right', 'top'),
    12: (1.265, -0.01, 'left', 'bottom'),
    13: (1.295, 0.01, 'right', 'top')
}

for i, channel in enumerate(channels):
    x, y = flow_means[i], flow_diffs[i]
    ha, va = ba_flow_positions[channel][2], ba_flow_positions[channel][3]
    
    ax3.annotate(f'{channel}', (x, y), 
                xytext=(8 if ha == 'right' else -8, 8 if va == 'top' else -8),
                textcoords='offset points',
                fontsize=8, ha=ha, va=va,
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8, linewidth=0.5),
                arrowprops=dict(arrowstyle='->', color='gray', lw=0.6, alpha=0.7))

ax3.set_xlabel('Average Mass Flow Rate (kg/s)', fontweight='bold', fontsize=11)
ax3.set_ylabel('Difference (RETA - Ref) (kg/s)', fontweight='bold', fontsize=11)
ax3.set_title('(C) Bland-Altman Plot: Mass Flow Rate', fontweight='bold', pad=15, fontsize=12)
ax3.legend(loc='upper right', fontsize=9, framealpha=0.9)
ax3.grid(True, alpha=0.3)

# 4. Bland-Altman图 (温度)
ax4 = fig.add_subplot(gs[1, 1])
temp_means = (sim_temp + ref_temp) / 2
temp_diffs = sim_temp - ref_temp
temp_mean_diff = np.mean(temp_diffs)
temp_std_diff = np.std(temp_diffs)

# 计算界限
upper_limit_temp = temp_mean_diff + 1.96 * temp_std_diff
lower_limit_temp = temp_mean_diff - 1.96 * temp_std_diff

ax4.axhline(temp_mean_diff, color='red', linestyle='-', alpha=0.8, 
            label=f'Mean: {temp_mean_diff:.2f}')
ax4.axhline(upper_limit_temp, color='red', linestyle='--', alpha=0.6, 
           label=f'+1.96 SD: {upper_limit_temp:.2f}')
ax4.axhline(lower_limit_temp, color='red', linestyle='--', alpha=0.6, 
           label=f'-1.96 SD: {lower_limit_temp:.2f}')

# 填充一致性界限区域
ax4.fill_between([min(temp_means), max(temp_means)], 
                lower_limit_temp, upper_limit_temp, 
                color='red', alpha=0.1)

scatter4 = ax4.scatter(temp_means, temp_diffs, c=channels, cmap='viridis', 
                      s=100, alpha=0.8, edgecolors='black', linewidth=0.5)

# Bland-Altman温度图的标注位置
ba_temp_positions = {
    1: (344.85, 0.7, 'left', 'top'),
    2: (347.0, 1.6, 'right', 'bottom'),
    3: (343.15, 0.7, 'left', 'top'),
    4: (348.55, 1.1, 'right', 'bottom'),
    5: (346.05, 0.5, 'left', 'top'),
    6: (347.85, 0.7, 'right', 'bottom'),
    7: (344.3, 0.8, 'left', 'top'),
    8: (348.6, 0.6, 'right', 'bottom'),
    9: (346.9, 0.4, 'left', 'top'),
    10: (345.5, 0.6, 'left', 'bottom'),
    11: (348.15, 0.7, 'right', 'top'),
    12: (346.35, 0.5, 'left', 'bottom'),
    13: (347.15, 0.5, 'right', 'top')
}

for i, channel in enumerate(channels):
    x, y = temp_means[i], temp_diffs[i]
    ha, va = ba_temp_positions[channel][2], ba_temp_positions[channel][3]
    
    ax4.annotate(f'{channel}', (x, y), 
                xytext=(8 if ha == 'right' else -8, 8 if va == 'top' else -8),
                textcoords='offset points',
                fontsize=8, ha=ha, va=va,
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8, linewidth=0.5),
                arrowprops=dict(arrowstyle='->', color='gray', lw=0.6, alpha=0.7))

ax4.set_xlabel('Average Outlet Temperature (K)', fontweight='bold', fontsize=11)
ax4.set_ylabel('Difference (RETA - Ref) (K)', fontweight='bold', fontsize=11)
ax4.set_title('(D) Bland-Altman Plot: Outlet Temperature', fontweight='bold', pad=15, fontsize=12)
ax4.legend(loc='upper right', fontsize=9, framealpha=0.9)
ax4.grid(True, alpha=0.3)

# 添加颜色条
cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
cbar = fig.colorbar(scatter1, cax=cbar_ax)
cbar.set_label('Channel Number', fontweight='bold', fontsize=11)

# 添加整体标题
fig.suptitle('Validation of Cooling Channel Simulation Model', 
             fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout()
plt.savefig('comprehensive_comparison.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('comprehensive_comparison.pdf', bbox_inches='tight', 
            facecolor='white', edgecolor='none')