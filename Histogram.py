import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ================================
#  手动输入你的数据
# ================================
# 13个通道的温度（单位: K 或 °C）

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

T_RETA = np.array([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13])   # 填入 RETA 的温度
T_SAM  = np.array([564,951,976,955,960,963,964,965,963,951,981,958,625])   # 填入 SAM 的温度

# 13个通道的流量 (kg/s 或 g/s)
M_RETA = np.array([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13])
M_SAM  = np.array([0.027,0.024,0.042,0.079,0.092,0.092,0.104,0.117,0.112,0.119,0.066,0.039,0.096])

channels = np.arange(1, 14)

# ================================
#  计算误差
# ================================
dT = T_RETA - T_SAM
dM = M_RETA - M_SAM

# ================================
#  绘图设置
# ================================
plt.rcParams.update({
    "font.size": 12,
    "font.family": "Times New Roman",
    "axes.linewidth": 1.2,
})

# ================================
#  图 1：温度误差条形图
# ================================
fig, ax = plt.subplots(figsize=(8, 4))

ax.bar(channels, dT, width=0.6, edgecolor="black")

ax.set_xlabel("Channel Number")
ax.set_ylabel("Temperature Error (RETA − SAM)")
ax.set_title("Coolant Outlet Temperature Error (Steady State)")

ax.grid(True, axis="y", linestyle="-", alpha=0.25)
ax.set_xticks(channels)

plt.tight_layout()
plt.show()


# ================================
#  图 2：流量误差条形图
# ================================
fig, ax = plt.subplots(figsize=(8, 4))

ax.bar(channels, dM, width=0.6, edgecolor="black")

ax.set_xlabel("Channel Number")
ax.set_ylabel("Mass Flow Rate Error (RETA − SAM)")
ax.set_title("Coolant Outlet Flow Rate Error (Steady State)")

ax.grid(True, axis="y", linestyle="-", alpha=0.25)
ax.set_xticks(channels)

plt.tight_layout()
plt.show()
