import pandas as pd
import matplotlib.pyplot as plt

class csvplot:
    def __init__(self):             
        self.ref_file_path = None
        self.model_file_path = None
    
    def model_file_read(self,file_path):     #读取模型数据
        self.model_data = pd.read_csv(file_path)
        self.selected_data = self.model_data.iloc[280:1766]

    def ref_file_read(self,file_paths_central,
                      file_paths_inner,
                      file_paths_middle,
                      file_paths_outer,
                      file_paths_side,
                      file_paths_Decay_heat,
                      file_paths_RCCS,
                      file_paths_radial_temp_central,
                      file_paths_radial_temp_core,
                      file_paths_radial_temp_side,
                      file_paths_radial_temp_permanent,
                      bk1_heat_outer_file_path,
                      bk5_heat_outer_file_path,
                      bk9_heat_outer_file_path,
                      bk1_side_in_file_path,
                      bk5_side_in_file_path,
                      bk9_side_in_file_path,
                      bk1_side_out_file_path,
                      bk5_side_out_file_path,
                      bk9_side_out_file_path,
                      bk1_per_file_path,
                      bk5_per_file_path,    
                      bk9_per_file_path,
                      bk1_vessel_file_path,
                      bk5_vessel_file_path,
                      bk9_vessel_file_path,
                      bk1_corebarrel_file_path,
                      bk5_corebarrel_file_path,
                      bk9_corebarrel_file_path,
                      bk1_heat_middle_file_path,
                      bk5_heat_middle_file_path,
                      bk9_heat_middle_file_path,
                      bk1_heat_inner_file_path,
                      bk5_heat_inner_file_path,
                      bk9_heat_inner_file_path,
                      bk1_center_in_file_path,
                      bk5_center_in_file_path,
                      bk9_center_in_file_path,
                      bk1_center_out_file_path,
                      bk5_center_out_file_path,
                      bk9_center_out_file_path,
                      bk1_heat_outer_file_path_RELAP,
                      bk5_heat_outer_file_path_RELAP,
                      bk9_heat_outer_file_path_RELAP,
                      bk1_side_in_file_path_RELAP,
                      bk5_side_in_file_path_RELAP,
                      bk9_side_in_file_path_RELAP,
                      bk1_side_out_file_path_RELAP,
                      bk5_side_out_file_path_RELAP,
                      bk9_side_out_file_path_RELAP,
                      bk1_per_file_path_RELAP,
                      bk5_per_file_path_RELAP,    
                      bk9_per_file_path_RELAP,
                      bk1_vessel_file_path_RELAP,
                      bk5_vessel_file_path_RELAP,
                      bk9_vessel_file_path_RELAP,
                      bk1_corebarrel_file_path_RELAP,
                      bk5_corebarrel_file_path_RELAP,
                      bk9_corebarrel_file_path_RELAP,
                      bk1_heat_middle_file_path_RELAP,
                      bk5_heat_middle_file_path_RELAP,
                      bk9_heat_middle_file_path_RELAP,
                      bk1_heat_inner_file_path_RELAP,
                      bk5_heat_inner_file_path_RELAP,
                      bk9_heat_inner_file_path_RELAP,
                      bk1_center_in_file_path_RELAP,
                      bk5_center_in_file_path_RELAP,
                      bk9_center_in_file_path_RELAP,
                      bk1_center_out_file_path_RELAP,
                      bk5_center_out_file_path_RELAP,
                      bk9_center_out_file_path_RELAP): 
        self.ref_data_central = pd.read_csv(file_paths_central)
        self.ref_data_inner = pd.read_csv(file_paths_inner)
        self.ref_data_middle = pd.read_csv(file_paths_middle)
        self.ref_data_outer = pd.read_csv(file_paths_outer)
        self.ref_data_side = pd.read_csv(file_paths_side)
        self.ref_data_Decay_heat = pd.read_csv(file_paths_Decay_heat)
        self.ref_data_RCCS = pd.read_csv(file_paths_RCCS)
        self.ref_data_radial_temp_central = pd.read_csv(file_paths_radial_temp_central)
        self.ref_data_radial_temp_core = pd.read_csv(file_paths_radial_temp_core)
        self.ref_data_radial_temp_side = pd.read_csv(file_paths_radial_temp_side)
        self.ref_data_radial_temp_permanent = pd.read_csv(file_paths_radial_temp_permanent)
        self.ref_bk1_heat_outer = pd.read_csv(bk1_heat_outer_file_path)
        self.ref_bk5_heat_outer = pd.read_csv(bk5_heat_outer_file_path)
        self.ref_bk9_heat_outer = pd.read_csv(bk9_heat_outer_file_path)
        self.ref_bk1_side_in = pd.read_csv(bk1_side_in_file_path)
        self.ref_bk5_side_in = pd.read_csv(bk5_side_in_file_path)
        self.ref_bk9_side_in = pd.read_csv(bk9_side_in_file_path)
        self.ref_bk1_side_out = pd.read_csv(bk1_side_out_file_path)
        self.ref_bk5_side_out = pd.read_csv(bk5_side_out_file_path)
        self.ref_bk9_side_out = pd.read_csv(bk9_side_out_file_path)
        self.ref_bk1_per = pd.read_csv(bk1_per_file_path)
        self.ref_bk5_per = pd.read_csv(bk5_per_file_path)
        self.ref_bk9_per = pd.read_csv(bk9_per_file_path)
        self.ref_bk1_vessel = pd.read_csv(bk1_vessel_file_path)
        self.ref_bk5_vessel = pd.read_csv(bk5_vessel_file_path)
        self.ref_bk9_vessel = pd.read_csv(bk9_vessel_file_path)
        self.ref_bk1_corebarrel = pd.read_csv(bk1_corebarrel_file_path)
        self.ref_bk5_corebarrel = pd.read_csv(bk5_corebarrel_file_path)
        self.ref_bk9_corebarrel = pd.read_csv(bk9_corebarrel_file_path)
        self.ref_bk1_heat_middle = pd.read_csv(bk1_heat_middle_file_path)
        self.ref_bk5_heat_middle = pd.read_csv(bk5_heat_middle_file_path)
        self.ref_bk9_heat_middle = pd.read_csv(bk9_heat_middle_file_path)
        self.ref_bk1_heat_inner = pd.read_csv(bk1_heat_inner_file_path)
        self.ref_bk5_heat_inner = pd.read_csv(bk5_heat_inner_file_path)
        self.ref_bk9_heat_inner = pd.read_csv(bk9_heat_inner_file_path)
        self.ref_bk1_center_in = pd.read_csv(bk1_center_in_file_path)
        self.ref_bk5_center_in = pd.read_csv(bk5_center_in_file_path)
        self.ref_bk9_center_in = pd.read_csv(bk9_center_in_file_path)
        self.ref_bk1_center_out = pd.read_csv(bk1_center_out_file_path)
        self.ref_bk5_center_out = pd.read_csv(bk5_center_out_file_path)
        self.ref_bk9_center_out = pd.read_csv(bk9_center_out_file_path)
        self.ref_bk1_heat_outer_RELAP = pd.read_csv(bk1_heat_outer_file_path_RELAP)
        self.ref_bk5_heat_outer_RELAP = pd.read_csv(bk5_heat_outer_file_path_RELAP)
        self.ref_bk9_heat_outer_RELAP = pd.read_csv(bk9_heat_outer_file_path_RELAP)
        self.ref_bk1_side_in_RELAP = pd.read_csv(bk1_side_in_file_path_RELAP)
        self.ref_bk5_side_in_RELAP = pd.read_csv(bk5_side_in_file_path_RELAP    )
        self.ref_bk9_side_in_RELAP = pd.read_csv(bk9_side_in_file_path_RELAP)
        self.ref_bk1_side_out_RELAP = pd.read_csv(bk1_side_out_file_path_RELAP)
        self.ref_bk5_side_out_RELAP = pd.read_csv(bk5_side_out_file_path_RELAP)
        self.ref_bk9_side_out_RELAP = pd.read_csv(bk9_side_out_file_path_RELAP)
        self.ref_bk1_per_RELAP = pd.read_csv(bk1_per_file_path_RELAP)
        self.ref_bk5_per_RELAP = pd.read_csv(bk5_per_file_path_RELAP)
        self.ref_bk9_per_RELAP = pd.read_csv(bk9_per_file_path_RELAP)
        self.ref_bk1_vessel_RELAP = pd.read_csv(bk1_vessel_file_path_RELAP)
        self.ref_bk5_vessel_RELAP = pd.read_csv(bk5_vessel_file_path_RELAP)
        self.ref_bk9_vessel_RELAP = pd.read_csv(bk9_vessel_file_path_RELAP)
        self.ref_bk1_corebarrel_RELAP = pd.read_csv(bk1_corebarrel_file_path_RELAP)
        self.ref_bk5_corebarrel_RELAP = pd.read_csv(bk5_corebarrel_file_path_RELAP)
        self.ref_bk9_corebarrel_RELAP = pd.read_csv(bk9_corebarrel_file_path_RELAP)
        self.ref_bk1_heat_middle_RELAP = pd.read_csv(bk1_heat_middle_file_path_RELAP)
        self.ref_bk5_heat_middle_RELAP = pd.read_csv(bk5_heat_middle_file_path_RELAP)
        self.ref_bk9_heat_middle_RELAP = pd.read_csv(bk9_heat_middle_file_path_RELAP)
        self.ref_bk1_heat_inner_RELAP = pd.read_csv(bk1_heat_inner_file_path_RELAP)
        self.ref_bk5_heat_inner_RELAP = pd.read_csv(bk5_heat_inner_file_path_RELAP)
        self.ref_bk9_heat_inner_RELAP = pd.read_csv(bk9_heat_inner_file_path_RELAP)
        self.ref_bk1_center_in_RELAP = pd.read_csv(bk1_center_in_file_path_RELAP)
        self.ref_bk5_center_in_RELAP = pd.read_csv(bk5_center_in_file_path_RELAP)
        self.ref_bk9_center_in_RELAP = pd.read_csv(bk9_center_in_file_path_RELAP)
        self.ref_bk1_center_out_RELAP = pd.read_csv(bk1_center_out_file_path_RELAP)
        self.ref_bk5_center_out_RELAP = pd.read_csv(bk5_center_out_file_path_RELAP)
        self.ref_bk9_center_out_RELAP = pd.read_csv(bk9_center_out_file_path_RELAP)
        
    def flow_compare(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13):         
        x_ref_central = self.ref_data_central.iloc[0:,0]
        y_ref_central = self.ref_data_central.iloc[0:,1]
        x_ref_inner = self.ref_data_inner.iloc[0:,0]
        y_ref_inner = self.ref_data_inner.iloc[0:,1]
        x_ref_middle = self.ref_data_middle.iloc[0:,0]
        y_ref_middle = self.ref_data_middle.iloc[0:,1]
        x_ref_outer = self.ref_data_outer.iloc[0:,0]
        y_ref_outer = self.ref_data_outer.iloc[0:,1]
        x_ref_side = self.ref_data_side.iloc[0:,0]
        y_ref_side = self.ref_data_side.iloc[0:,1]

        x_model = self.selected_data[a]/3600
        y_model_central = self.selected_data[b1]
        y_model_inner = self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5]
        y_model_middle = self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9]
        y_model_outer = self.selected_data[b10] + self.selected_data[b11] + self.selected_data[b12]
        y_model_side = self.selected_data[b13]
        sum = y_model_central + y_model_inner + y_model_middle + y_model_outer + y_model_side
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
            'legend.markerscale': 0.6,
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
        plt.figure(figsize=(7,10))
        plt.plot(x_ref_central, y_ref_central,label='central channel_ref',linestyle=':',color='orange')
        plt.plot(x_ref_inner, y_ref_inner,label='inner channel_ref',linestyle=':',color='blue')
        plt.plot(x_ref_middle, y_ref_middle,label='middle channel_ref',linestyle=':',color='red')
        plt.plot(x_ref_outer, y_ref_outer,label='outer channel_ref',linestyle=':',color='green')
        plt.plot(x_ref_side, y_ref_side,label='side channel_ref',linestyle=':',color='purple')
        plt.plot(x_model, y_model_central,label='center channel',color='orange',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.plot(x_model, y_model_inner,label='inner channel',color='blue',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.plot(x_model, y_model_middle,label='middle channel',color='red',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.plot(x_model, y_model_outer,label='outer channel',color='green',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.plot(x_model, y_model_side,label='side channel',color='purple',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.xlabel('Time (h)')
        plt.ylabel('Mass flow rate (kg/s)')
        plt.title('Flow rate comparison')
        plt.legend(shadow=True, frameon=True)
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def power_compare(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12):
        x_ref_RCCS = self.ref_data_RCCS.iloc[0:,0]
        y_ref_RCCS = self.ref_data_RCCS.iloc[0:,1]
        x_ref_Decay_heat = self.ref_data_Decay_heat.iloc[0:,0]
        y_ref_Decay_heat = self.ref_data_Decay_heat.iloc[0:,1]
        x_model = self.selected_data[a]/3600
        y_model_Decay_heat = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10])/1000
        y_model_RCCS = (self.selected_data[b11] + self.selected_data[b12])/1000
        plt.figure(figsize=(10,8))

        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
            'xtick.labelsize': 18,         # X轴刻度字号
            'ytick.labelsize': 18,         # Y轴刻度字号
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
        
        #plt.plot(x_ref_RCCS, y_ref_RCCS,label='RCCS_ref',linestyle='--',color='blue')
        #plt.plot(x_ref_Decay_heat, y_ref_Decay_heat,label='Decay_heat_ref',linestyle='--',color='orange')
        #plt.plot(x_model, y_model_RCCS,label='RCCS',color='blue')
        plt.plot(x_model, y_model_Decay_heat,label='Decay_heat',color='orange',linewidth=4)
        plt.xlabel('Time (h)')
        plt.ylabel('Power (kW)')
        plt.title('Decay heat curve',fontsize=18)
        plt.legend(shadow=True, frameon=True,fontsize=18)
        plt.grid(False, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def radial_block1_temp_compare(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,b61,b62,b63,b64,b65,b66,b67,b68,b69,b70,b71,b72,b73,b74,b75,b76,b77,b78,b79,b80,b81,b82,b83,b84,b85,b86,b87,b88,b89,b90,b91,b92,b93,b94,b95,b96,b97,b98,b99,b100,b101,b102,b103,b104,b105,b106,b107,b108,b109,b110,b111,b112,b113,b114,b115,b116,b117,b118,b119,b120,b121,b122,b123,b124,b125,b126,b127,b128,b129,b130,b131,b132,b133,b134,b135,b136,b137,b138,b139,b140,b141,b142,b143,b144,b145,b146,b147,b148,b149,b150,b151,b152,b153,b154,b155,b156,b157,b158,b159,b160,b161,b162,b163,b164,b165,b166,b167,b168,b169,b170,b171,b172,b173,b174,b175,b176,b177,b178,b179,b180,b181,b182,b183,b184,b185,b186,b187,b188,b189,b190,b191,b192,b193,b194,b195,b196,b197,b198,b199,b200,b201,b202,b203,b204,b205,b206,b207,b208,b209,b210,b211,b212,b213,b214,b215,b216,b217,b218,b219,b220,b221,b222,b223,b224,b225,b226,b227,b228,b229,b230,b231,b232,b233,b234,b235,b236,b237,b238,b239,b240,b241,b242,b243,b244,b245,b246,b247,b248,b249,b250):
        x_ref_radial_temp_central = self.ref_data_radial_temp_central.iloc[0:,0]
        y_ref_radial_temp_central = self.ref_data_radial_temp_central.iloc[0:,1]
        x_ref_radial_temp_core = self.ref_data_radial_temp_core.iloc[0:,0]
        y_ref_radial_temp_core = self.ref_data_radial_temp_core.iloc[0:,1]
        x_ref_radial_temp_side = self.ref_data_radial_temp_side.iloc[0:,0]
        y_ref_radial_temp_side = self.ref_data_radial_temp_side.iloc[0:,1]
        x_ref_radial_temp_permanent = self.ref_data_radial_temp_permanent.iloc[0:,0]
        y_ref_radial_temp_permanent = self.ref_data_radial_temp_permanent.iloc[0:,1]
        x_model = self.selected_data[a]/3600
        y_model_radial_temp_central = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10] + self.selected_data[b11] + self.selected_data[b12] + self.selected_data[b13] + self.selected_data[b14] + self.selected_data[b15] + self.selected_data[b16] + self.selected_data[b17] + self.selected_data[b18] + self.selected_data[b19] + self.selected_data[b20])/20
        y_model_radial_temp_core = (self.selected_data[b21] + self.selected_data[b22] + self.selected_data[b23] + self.selected_data[b24] + self.selected_data[b25] + self.selected_data[b26] + self.selected_data[b27] + self.selected_data[b28] + self.selected_data[b29] + self.selected_data[b30] + self.selected_data[b31] + self.selected_data[b32] + self.selected_data[b33] + self.selected_data[b34] + self.selected_data[b35] + self.selected_data[b36] + self.selected_data[b37] + self.selected_data[b38] + self.selected_data[b39] + self.selected_data[b40] + self.selected_data[b41] + self.selected_data[b42] + self.selected_data[b43] + self.selected_data[b44] + self.selected_data[b45] + self.selected_data[b46] + self.selected_data[b47] + self.selected_data[b48] + self.selected_data[b49] + self.selected_data[b50] + self.selected_data[b51] + self.selected_data[b52] + self.selected_data[b53] + self.selected_data[b54] + self.selected_data[b55] + self.selected_data[b56] + self.selected_data[b57] + self.selected_data[b58] + self.selected_data[b59] + self.selected_data[b60] + self.selected_data[b61] + self.selected_data[b62] + self.selected_data[b63] + self.selected_data[b64] + self.selected_data[b65] + self.selected_data[b66] + self.selected_data[b67] + self.selected_data[b68] + self.selected_data[b69] + self.selected_data[b70] + self.selected_data[b71] + self.selected_data[b72] + self.selected_data[b73] + self.selected_data[b74] + self.selected_data[b75] + self.selected_data[b76] + self.selected_data[b77] + self.selected_data[b78] + self.selected_data[b79] + self.selected_data[b80] + self.selected_data[b81] + self.selected_data[b82] + self.selected_data[b83] + self.selected_data[b84] + self.selected_data[b85] + self.selected_data[b86] + self.selected_data[b87] + self.selected_data[b88] + self.selected_data[b89] + self.selected_data[b90] + self.selected_data[b91] + self.selected_data[b92] + self.selected_data[b93] + self.selected_data[b94] + self.selected_data[b95] + self.selected_data[b96] + self.selected_data[b97] + self.selected_data[b98] + self.selected_data[b99] + self.selected_data[b100] + self.selected_data[b101] + self.selected_data[b102] + self.selected_data[b103] + self.selected_data[b104] + self.selected_data[b105] + self.selected_data[b106] + self.selected_data[b107] + self.selected_data[b108] + self.selected_data[b109] + self.selected_data[b110] + self.selected_data[b111] + self.selected_data[b112] + self.selected_data[b113] + self.selected_data[b114] + self.selected_data[b115] + self.selected_data[b116] + self.selected_data[b117] + self.selected_data[b118] + self.selected_data[b119] + self.selected_data[b120] + self.selected_data[b121] + self.selected_data[b122] + self.selected_data[b123] + self.selected_data[b124] + self.selected_data[b125] + self.selected_data[b126] + self.selected_data[b127] + self.selected_data[b128] + self.selected_data[b129] + self.selected_data[b130] + self.selected_data[b131] + self.selected_data[b132] + self.selected_data[b133] + self.selected_data[b134] + self.selected_data[b135] + self.selected_data[b136] + self.selected_data[b137] + self.selected_data[b138] + self.selected_data[b139] + self.selected_data[b140] + self.selected_data[b141] + self.selected_data[b142] + self.selected_data[b143] + self.selected_data[b144] + self.selected_data[b145] + self.selected_data[b146] + self.selected_data[b147] + self.selected_data[b148] + self.selected_data[b149] + self.selected_data[b150] + self.selected_data[b151] + self.selected_data[b152] + self.selected_data[b153] + self.selected_data[b154] + self.selected_data[b155] + self.selected_data[b156] + self.selected_data[b157] + self.selected_data[b158] + self.selected_data[b159] + self.selected_data[b160] + self.selected_data[b161] + self.selected_data[b162] + self.selected_data[b163] + self.selected_data[b164] + self.selected_data[b165] + self.selected_data[b166] + self.selected_data[b167] + self.selected_data[b168] + self.selected_data[b169] + self.selected_data[b170] + self.selected_data[b171] + self.selected_data[b172] + self.selected_data[b173] + self.selected_data[b174] + self.selected_data[b175] + self.selected_data[b176] + self.selected_data[b177] + self.selected_data[b178] + self.selected_data[b179] + self.selected_data[b180] + self.selected_data[b181] + self.selected_data[b182] + self.selected_data[b183] + self.selected_data[b184] + self.selected_data[b185] + self.selected_data[b186] + self.selected_data[b187] + self.selected_data[b188] + self.selected_data[b189] + self.selected_data[b190] + self.selected_data[b191] + self.selected_data[b192] + self.selected_data[b193] + self.selected_data[b194] + self.selected_data[b195] + self.selected_data[b196] + self.selected_data[b197] + self.selected_data[b198] + self.selected_data[b199] + self.selected_data[b200] + self.selected_data[b201] + self.selected_data[b202] + self.selected_data[b203] + self.selected_data[b204] + self.selected_data[b205] + self.selected_data[b206] + self.selected_data[b207] + self.selected_data[b208] + self.selected_data[b209] + self.selected_data[b210] + self.selected_data[b211] + self.selected_data[b212] + self.selected_data[b213] + self.selected_data[b214] + self.selected_data[b215] + self.selected_data[b216] + self.selected_data[b217] + self.selected_data[b218] + self.selected_data[b219] + self.selected_data[b220])/200
        y_model_radial_temp_side = (self.selected_data[b221] + self.selected_data[b222] + self.selected_data[b223] + self.selected_data[b224] + self.selected_data[b225] + self.selected_data[b226] + self.selected_data[b227] + self.selected_data[b228] + self.selected_data[b229] + self.selected_data[b230] + self.selected_data[b231] + self.selected_data[b232] + self.selected_data[b233] + self.selected_data[b234] + self.selected_data[b235] + self.selected_data[b236] + self.selected_data[b237] + self.selected_data[b238] + self.selected_data[b239] + self.selected_data[b240])/20
        y_model_radial_temp_permanent = (self.selected_data[b241] + self.selected_data[b242] + self.selected_data[b243] + self.selected_data[b244] + self.selected_data[b245] + self.selected_data[b246] + self.selected_data[b247] + self.selected_data[b248] + self.selected_data[b249] + self.selected_data[b250])/10
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.figure(figsize=(7,10))
        plt.plot(x_ref_radial_temp_central, y_ref_radial_temp_central,label='central_ref',linestyle='--',color='lightblue',marker='^', markersize=5, markevery=len(x_ref_radial_temp_central)//10)
        plt.plot(x_ref_radial_temp_core, y_ref_radial_temp_core,label='core_ref',linestyle='--',color='red',marker='^', markersize=5, markevery=len(x_ref_radial_temp_core)//10)
        plt.plot(x_ref_radial_temp_side, y_ref_radial_temp_side,label='side_ref',linestyle='--',color='purple',marker='^', markersize=5, markevery=len(x_ref_radial_temp_side)//10)
        plt.plot(x_ref_radial_temp_permanent, y_ref_radial_temp_permanent,label='permanent_ref',linestyle='--',color='green',marker='^', markersize=5, markevery=len(x_ref_radial_temp_permanent)//10)
        plt.plot(x_model, y_model_radial_temp_central,label='central',color='lightblue',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.plot(x_model, y_model_radial_temp_core,label='core',color='red',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.plot(x_model, y_model_radial_temp_side,label='side',color='purple',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.plot(x_model, y_model_radial_temp_permanent,label='permanent',color='green',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.xlabel('Time (h)')
        plt.ylabel('Temperature (K)')
        plt.title('Radial block 1 temperature comparison')
        plt.legend(shadow=True, frameon=True, fontsize=6,loc='best')
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()


    def axial_center_in(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30):
        x1_ref = self.ref_bk1_center_in.iloc[0:,0] 
        y1_ref = self.ref_bk1_center_in.iloc[0:,1]
        x5_ref = self.ref_bk5_center_in.iloc[0:,0]
        y5_ref = self.ref_bk5_center_in.iloc[0:,1]
        x9_ref = self.ref_bk9_center_in.iloc[0:,0]    
        y9_ref = self.ref_bk9_center_in.iloc[0:,1]

        x1_ref_RELAP = self.ref_bk1_center_in_RELAP.iloc[0:,0] 
        y1_ref_RELAP = self.ref_bk1_center_in_RELAP.iloc[0:,1]
        x5_ref_RELAP = self.ref_bk5_center_in_RELAP.iloc[0:,0]
        y5_ref_RELAP = self.ref_bk5_center_in_RELAP.iloc[0:,1]
        x9_ref_RELAP = self.ref_bk9_center_in_RELAP.iloc[0:,0]    
        y9_ref_RELAP = self.ref_bk9_center_in_RELAP.iloc[0:,1]

        x_model = self.selected_data[a]/3600    
        y1_model = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10])/10
        y5_model = (self.selected_data[b11] + self.selected_data[b12] + self.selected_data[b13] + self.selected_data[b14] + self.selected_data[b15] + self.selected_data[b16] + self.selected_data[b17] + self.selected_data[b18] + self.selected_data[b19] + self.selected_data[b20])/10
        y9_model = (self.selected_data[b21] + self.selected_data[b22] + self.selected_data[b23] + self.selected_data[b24] + self.selected_data[b25] + self.selected_data[b26] + self.selected_data[b27] + self.selected_data[b28] + self.selected_data[b29] + self.selected_data[b30])/10
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.figure(figsize=(7,10))
        plt.plot(x1_ref, y1_ref,label='bk1_SAM',linestyle='--',color='red',marker='v', markersize=5, markevery=len(x1_ref)//10)
        plt.plot(x5_ref, y5_ref,label='bk5_SAM',linestyle='--',color='blue',marker='v', markersize=5, markevery=len(x1_ref)//10)   
        plt.plot(x9_ref, y9_ref,label='bk9_SAM',linestyle='--',color='green',marker='v', markersize=5, markevery=len(x1_ref)//10)  
        plt.plot(x1_ref_RELAP, y1_ref_RELAP,label='bk1_RELAP5',linestyle=':',color='red',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10)
        plt.plot(x5_ref_RELAP, y5_ref_RELAP,label='bk5_RELAP5',linestyle=':',color='blue',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10)
        plt.plot(x9_ref_RELAP, y9_ref_RELAP,label='bk9_RELAP5',linestyle=':',color='green',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10)
        plt.plot(x_model, y1_model,label='bk1_center_in',color='red',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.plot(x_model, y5_model,label='bk5_center_in',color='blue',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.plot(x_model, y9_model,label='bk9_center_in',color='green',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.xlabel('Time (h)')
        plt.ylabel('Temperature (K)')
        plt.title('Axial center_in reflector temperature comparison')
        plt.legend(shadow=True, frameon=True, fontsize=4, loc='upper right',markerscale=0.5)
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def axial_center_out(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30):
        x1_ref = self.ref_bk1_center_out.iloc[0:,0] 
        y1_ref = self.ref_bk1_center_out.iloc[0:,1]
        x5_ref = self.ref_bk5_center_out.iloc[0:,0]
        y5_ref = self.ref_bk5_center_out.iloc[0:,1]
        x9_ref = self.ref_bk9_center_out.iloc[0:,0]    
        y9_ref = self.ref_bk9_center_out.iloc[0:,1]   

        x1_ref_RELAP = self.ref_bk1_center_out_RELAP.iloc[0:,0] 
        y1_ref_RELAP = self.ref_bk1_center_out_RELAP.iloc[0:,1]
        x5_ref_RELAP = self.ref_bk5_center_out_RELAP.iloc[0:,0]
        y5_ref_RELAP = self.ref_bk5_center_out_RELAP.iloc[0:,1]
        x9_ref_RELAP = self.ref_bk9_center_out_RELAP.iloc[0:,0]    
        y9_ref_RELAP = self.ref_bk9_center_out_RELAP.iloc[0:,1]    

        x_model = self.selected_data[a]/3600    
        y1_model = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10])/10
        y5_model = (self.selected_data[b11] + self.selected_data[b12] + self.selected_data[b13] + self.selected_data[b14] + self.selected_data[b15] + self.selected_data[b16] + self.selected_data[b17] + self.selected_data[b18] + self.selected_data[b19] + self.selected_data[b20])/10
        y9_model = (self.selected_data[b21] + self.selected_data[b22] + self.selected_data[b23] + self.selected_data[b24] + self.selected_data[b25] + self.selected_data[b26] + self.selected_data[b27] + self.selected_data[b28] + self.selected_data[b29] + self.selected_data[b30])/10
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.figure(figsize=(7,10))
        plt.plot(x1_ref, y1_ref,label='bk1_SAM',linestyle='--',color='red')
        plt.plot(x5_ref, y5_ref,label='bk5_SAM',linestyle='--',color='blue')  
        plt.plot(x9_ref, y9_ref,label='bk9_SAM',linestyle='--',color='green')    
        plt.plot(x1_ref_RELAP, y1_ref_RELAP,label='bk1_RELAP5',linestyle=':',color='red')
        plt.plot(x5_ref_RELAP, y5_ref_RELAP,label='bk5_RELAP5',linestyle=':',color='blue')  
        plt.plot(x9_ref_RELAP, y9_ref_RELAP,label='bk9_RELAP5',linestyle=':',color='green')     
        plt.plot(x_model, y1_model,label='bk1_center_out',color='red',linewidth=2)    
        plt.plot(x_model, y5_model,label='bk5_center_out',color='blue',linewidth=2)    
        plt.plot(x_model, y9_model,label='bk9_center_out',color='green',linewidth=2)    
        plt.xlabel('Time (h)')
        plt.ylabel('Temperature (K)')
        plt.title('Axial center_out reflector temperature comparison')
        plt.legend(shadow=True, frameon=True, fontsize=6, loc='best')
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def axial_heat_inner(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,b61,b62,b63,b64,b65,b66,b67,b68,b69,b70,b71,b72,b73,b74,b75,b76,b77,b78,b79,b80,b81,b82,b83,b84,b85,b86,b87,b88,b89,b90):
        x1_ref = self.ref_bk1_heat_inner.iloc[0:,0]
        y1_ref = self.ref_bk1_heat_inner.iloc[0:,1]
        x5_ref = self.ref_bk5_heat_inner.iloc[0:,0]
        y5_ref = self.ref_bk5_heat_inner.iloc[0:,1]
        x9_ref = self.ref_bk9_heat_inner.iloc[0:,0]
        y9_ref = self.ref_bk9_heat_inner.iloc[0:,1]

        x1_ref_RELAP = self.ref_bk1_heat_inner_RELAP.iloc[0:,0]
        y1_ref_RELAP = self.ref_bk1_heat_inner_RELAP.iloc[0:,1]
        x5_ref_RELAP = self.ref_bk5_heat_inner_RELAP.iloc[0:,0]
        y5_ref_RELAP = self.ref_bk5_heat_inner_RELAP.iloc[0:,1]
        x9_ref_RELAP = self.ref_bk9_heat_inner_RELAP.iloc[0:,0]
        y9_ref_RELAP = self.ref_bk9_heat_inner_RELAP.iloc[0:,1]
        
        x_model = self.selected_data[a]/3600
        y_model_axial_temp_1 = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10] + self.selected_data[b11] + self.selected_data[b12] + self.selected_data[b13] + self.selected_data[b14] + self.selected_data[b15] + self.selected_data[b16] + self.selected_data[b17] + self.selected_data[b18] + self.selected_data[b19] + self.selected_data[b20] + self.selected_data[b21] + self.selected_data[b22] + self.selected_data[b23] + self.selected_data[b24] + self.selected_data[b25] + self.selected_data[b26] + self.selected_data[b27] + self.selected_data[b28] + self.selected_data[b29] + self.selected_data[b30])/30
        y_model_axial_temp_5 = (self.selected_data[b31] + self.selected_data[b32] + self.selected_data[b33] + self.selected_data[b34] + self.selected_data[b35] + self.selected_data[b36] + self.selected_data[b37] + self.selected_data[b38] + self.selected_data[b39] + self.selected_data[b40] + self.selected_data[b41] + self.selected_data[b42] + self.selected_data[b43] + self.selected_data[b44] + self.selected_data[b45] + self.selected_data[b46] + self.selected_data[b47] + self.selected_data[b48] + self.selected_data[b49] + self.selected_data[b50] + self.selected_data[b51] + self.selected_data[b52] + self.selected_data[b53] + self.selected_data[b54] + self.selected_data[b55] + self.selected_data[b56] + self.selected_data[b57] + self.selected_data[b58] + self.selected_data[b59] + self.selected_data[b60])/30
        y_model_axial_temp_9 = (self.selected_data[b61] + self.selected_data[b62] + self.selected_data[b63] + self.selected_data[b64] + self.selected_data[b65] + self.selected_data[b66] + self.selected_data[b67] + self.selected_data[b68] + self.selected_data[b69] + self.selected_data[b70] + self.selected_data[b71] + self.selected_data[b72] + self.selected_data[b73] + self.selected_data[b74] + self.selected_data[b75] + self.selected_data[b76] + self.selected_data[b77] + self.selected_data[b78] + self.selected_data[b79] + self.selected_data[b80] + self.selected_data[b81] + self.selected_data[b82] + self.selected_data[b83] + self.selected_data[b84] + self.selected_data[b85] + self.selected_data[b86] + self.selected_data[b87] + self.selected_data[b88] + self.selected_data[b89] + self.selected_data[b90])/30
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.figure(figsize=(7,10))
        plt.plot(x1_ref, y1_ref,label='bk1_SAM',linestyle='--',color='red')
        plt.plot(x5_ref, y5_ref,label='bk5_SAM',linestyle='--',color='blue')
        plt.plot(x9_ref, y9_ref,label='bk9_SAM',linestyle='--',color='green')
        plt.plot(x1_ref_RELAP, y1_ref_RELAP,label='bk1_RELAP5',linestyle=':',color='red')
        plt.plot(x5_ref_RELAP, y5_ref_RELAP,label='bk5_RELAP5',linestyle=':',color='blue')
        plt.plot(x9_ref_RELAP, y9_ref_RELAP,label='bk9_RELAP5',linestyle=':',color='green')
        plt.plot(x_model, y_model_axial_temp_1,label='bk1',color='red',linewidth=2)
        plt.plot(x_model, y_model_axial_temp_5,label='bk5',color='blue',linewidth=2)
        plt.plot(x_model, y_model_axial_temp_9,label='bk9',color='green',linewidth=2)
        plt.xlabel('Time (h)')
        plt.ylabel('Temperature (K)')
        plt.title('Axial heat block inner temperature comparison')
        plt.legend(shadow=True, frameon=True,loc='best')
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def axial_heat_middle(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,b61,b62,b63,b64,b65,b66,b67,b68,b69,b70,b71,b72,b73,b74,b75,b76,b77,b78,b79,b80,b81,b82,b83,b84,b85,b86,b87,b88,b89,b90,b91,b92,b93,b94,b95,b96,b97,b98,b99,b100,b101,b102,b103,b104,b105,b106,b107,b108,b109,b110,b111,b112,b113,b114,b115,b116,b117,b118,b119,b120):
        x1_ref = self.ref_bk1_heat_middle.iloc[0:,0]
        y1_ref = self.ref_bk1_heat_middle.iloc[0:,1]
        x5_ref = self.ref_bk5_heat_middle.iloc[0:,0]
        y5_ref = self.ref_bk5_heat_middle.iloc[0:,1]
        x9_ref = self.ref_bk9_heat_middle.iloc[0:,0]
        y9_ref = self.ref_bk9_heat_middle.iloc[0:,1]

        x1_ref_RELAP = self.ref_bk1_heat_middle_RELAP.iloc[0:,0]
        y1_ref_RELAP = self.ref_bk1_heat_middle_RELAP.iloc[0:,1]
        x5_ref_RELAP = self.ref_bk5_heat_middle_RELAP.iloc[0:,0]
        y5_ref_RELAP = self.ref_bk5_heat_middle_RELAP.iloc[0:,1]
        x9_ref_RELAP = self.ref_bk9_heat_middle_RELAP.iloc[0:,0]
        y9_ref_RELAP = self.ref_bk9_heat_middle_RELAP.iloc[0:,1]

        x_model = self.selected_data[a]/3600
        y_model_axial_temp_1 = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10] + self.selected_data[b11] + self.selected_data[b12] + self.selected_data[b13] + self.selected_data[b14] + self.selected_data[b15] + self.selected_data[b16] + self.selected_data[b17] + self.selected_data[b18] + self.selected_data[b19] + self.selected_data[b20] + self.selected_data[b21] + self.selected_data[b22] + self.selected_data[b23] + self.selected_data[b24] + self.selected_data[b25] + self.selected_data[b26] + self.selected_data[b27] + self.selected_data[b28] + self.selected_data[b29] + self.selected_data[b30] + self.selected_data[b31] + self.selected_data[b32] + self.selected_data[b33] + self.selected_data[b34] + self.selected_data[b35] + self.selected_data[b36] + self.selected_data[b37] + self.selected_data[b38] + self.selected_data[b39] + self.selected_data[b40])/40
        y_model_axial_temp_5 = (self.selected_data[b41] + self.selected_data[b42] + self.selected_data[b43] + self.selected_data[b44] + self.selected_data[b45] + self.selected_data[b46] + self.selected_data[b47] + self.selected_data[b48] + self.selected_data[b49] + self.selected_data[b50] + self.selected_data[b51] + self.selected_data[b52] + self.selected_data[b53] + self.selected_data[b54] + self.selected_data[b55] + self.selected_data[b56] + self.selected_data[b57] + self.selected_data[b58] + self.selected_data[b59] + self.selected_data[b60] + self.selected_data[b61] + self.selected_data[b62] + self.selected_data[b63] + self.selected_data[b64] + self.selected_data[b65] + self.selected_data[b66] + self.selected_data[b67] + self.selected_data[b68] + self.selected_data[b69] + self.selected_data[b70] + self.selected_data[b71] + self.selected_data[b72] + self.selected_data[b73] + self.selected_data[b74] + self.selected_data[b75] + self.selected_data[b76] + self.selected_data[b77] + self.selected_data[b78] + self.selected_data[b79] + self.selected_data[b80])/40
        y_model_axial_temp_9 = (self.selected_data[b81] + self.selected_data[b82] + self.selected_data[b83] + self.selected_data[b84] + self.selected_data[b85] + self.selected_data[b86] + self.selected_data[b87] + self.selected_data[b88] + self.selected_data[b89] + self.selected_data[b90] + self.selected_data[b91] + self.selected_data[b92] + self.selected_data[b93] + self.selected_data[b94] + self.selected_data[b95] + self.selected_data[b96] + self.selected_data[b97] + self.selected_data[b98] + self.selected_data[b99] + self.selected_data[b100] + self.selected_data[b101] + self.selected_data[b102] + self.selected_data[b103] + self.selected_data[b104] + self.selected_data[b105] + self.selected_data[b106] + self.selected_data[b107] + self.selected_data[b108] + self.selected_data[b109] + self.selected_data[b110] + self.selected_data[b111] + self.selected_data[b112] + self.selected_data[b113] + self.selected_data[b114] + self.selected_data[b115] + self.selected_data[b116] + self.selected_data[b117] + self.selected_data[b118] + self.selected_data[b119] + self.selected_data[b120])/40
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.figure(figsize=(7,10))
        plt.plot(x1_ref, y1_ref,label='bk1_SAM',linestyle='--',color='red')
        plt.plot(x5_ref, y5_ref,label='bk5_SAM',linestyle='--',color='blue')
        plt.plot(x9_ref, y9_ref,label='bk9_SAM',linestyle='--',color='green')
        plt.plot(x1_ref_RELAP, y1_ref_RELAP,label='bk1_RELAP5',linestyle=':',color='red')
        plt.plot(x5_ref_RELAP, y5_ref_RELAP,label='bk5_RELAP5',linestyle=':',color='blue')
        plt.plot(x9_ref_RELAP, y9_ref_RELAP,label='bk9_RELAP5',linestyle=':',color='green')
        plt.plot(x_model, y_model_axial_temp_1,label='bk1',color='red',linewidth=2)
        plt.plot(x_model, y_model_axial_temp_5,label='bk5',color='blue',linewidth=2)
        plt.plot(x_model, y_model_axial_temp_9,label='bk9',color='green',linewidth=2)
        plt.xlabel('Time (h)')
        plt.ylabel('Temperature (K)')
        plt.title('Axial heating block middle temperature comparison')
        plt.legend(shadow=True, frameon=True,loc='best')
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def axial_heat_outer(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,b61,b62,b63,b64,b65,b66,b67,b68,b69,b70,b71,b72,b73,b74,b75,b76,b77,b78,b79,b80,b81,b82,b83,b84,b85,b86,b87,b88,b89,b90,b91,b92,b93,b94,b95,b96,b97,b98,b99,b100,b101,b102,b103,b104,b105,b106,b107,b108,b109,b110,b111,b112,b113,b114,b115,b116,b117,b118,b119,b120):
        x1_ref = self.ref_bk1_heat_outer.iloc[0:,0]
        y1_ref = self.ref_bk1_heat_outer.iloc[0:,1]
        x5_ref = self.ref_bk5_heat_outer.iloc[0:,0]
        y5_ref = self.ref_bk5_heat_outer.iloc[0:,1]
        x9_ref = self.ref_bk9_heat_outer.iloc[0:,0]
        y9_ref = self.ref_bk9_heat_outer.iloc[0:,1]

        x1_ref_RELAP = self.ref_bk1_heat_outer_RELAP.iloc[0:,0]
        y1_ref_RELAP = self.ref_bk1_heat_outer_RELAP.iloc[0:,1]
        x5_ref_RELAP = self.ref_bk5_heat_outer_RELAP.iloc[0:,0]
        y5_ref_RELAP = self.ref_bk5_heat_outer_RELAP.iloc[0:,1]
        x9_ref_RELAP = self.ref_bk9_heat_outer_RELAP.iloc[0:,0]
        y9_ref_RELAP = self.ref_bk9_heat_outer_RELAP.iloc[0:,1]

        x_model = self.selected_data[a]/3600
        y_model_axial_temp_1 = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10] + self.selected_data[b11] + self.selected_data[b12] + self.selected_data[b13] + self.selected_data[b14] + self.selected_data[b15] + self.selected_data[b16] + self.selected_data[b17] + self.selected_data[b18] + self.selected_data[b19] + self.selected_data[b20] + self.selected_data[b21] + self.selected_data[b22] + self.selected_data[b23] + self.selected_data[b24] + self.selected_data[b25] + self.selected_data[b26] + self.selected_data[b27] + self.selected_data[b28] + self.selected_data[b29] + self.selected_data[b30] + self.selected_data[b31] + self.selected_data[b32] + self.selected_data[b33] + self.selected_data[b34] + self.selected_data[b35] + self.selected_data[b36] + self.selected_data[b37] + self.selected_data[b38] + self.selected_data[b39] + self.selected_data[b40])/40
        y_model_axial_temp_5 = (self.selected_data[b41] + self.selected_data[b42] + self.selected_data[b43] + self.selected_data[b44] + self.selected_data[b45] + self.selected_data[b46] + self.selected_data[b47] + self.selected_data[b48] + self.selected_data[b49] + self.selected_data[b50] + self.selected_data[b51] + self.selected_data[b52] + self.selected_data[b53] + self.selected_data[b54] + self.selected_data[b55] + self.selected_data[b56] + self.selected_data[b57] + self.selected_data[b58] + self.selected_data[b59] + self.selected_data[b60] + self.selected_data[b61] + self.selected_data[b62] + self.selected_data[b63] + self.selected_data[b64] + self.selected_data[b65] + self.selected_data[b66] + self.selected_data[b67] + self.selected_data[b68] + self.selected_data[b69] + self.selected_data[b70] + self.selected_data[b71] + self.selected_data[b72] + self.selected_data[b73] + self.selected_data[b74] + self.selected_data[b75] + self.selected_data[b76] + self.selected_data[b77] + self.selected_data[b78] + self.selected_data[b79] + self.selected_data[b80])/40
        y_model_axial_temp_9 = (self.selected_data[b81] + self.selected_data[b82] + self.selected_data[b83] + self.selected_data[b84] + self.selected_data[b85] + self.selected_data[b86] + self.selected_data[b87] + self.selected_data[b88] + self.selected_data[b89] + self.selected_data[b90] + self.selected_data[b91] + self.selected_data[b92] + self.selected_data[b93] + self.selected_data[b94] + self.selected_data[b95] + self.selected_data[b96] + self.selected_data[b97] + self.selected_data[b98] + self.selected_data[b99] + self.selected_data[b100] + self.selected_data[b101] + self.selected_data[b102] + self.selected_data[b103] + self.selected_data[b104] + self.selected_data[b105] + self.selected_data[b106] + self.selected_data[b107] + self.selected_data[b108] + self.selected_data[b109] + self.selected_data[b110] + self.selected_data[b111] + self.selected_data[b112] + self.selected_data[b113] + self.selected_data[b114] + self.selected_data[b115] + self.selected_data[b116] + self.selected_data[b117] + self.selected_data[b118] + self.selected_data[b119] + self.selected_data[b120])/40
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.figure(figsize=(7,10))
        plt.plot(x1_ref, y1_ref,label='bk1_SAM',linestyle='--',color='red',marker='v', markersize=5, markevery=len(x1_ref)//10)
        plt.plot(x5_ref, y5_ref,label='bk5_SAM',linestyle='--',color='blue',marker='v', markersize=5, markevery=len(x1_ref)//10)
        plt.plot(x9_ref, y9_ref,label='bk9_SAM',linestyle='--',color='green',marker='v', markersize=5, markevery=len(x1_ref)//10)
        plt.plot(x1_ref_RELAP, y1_ref_RELAP,label='bk1_RELAP5',linestyle=':',color='red',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10)
        plt.plot(x5_ref_RELAP, y5_ref_RELAP,label='bk5_RELAP5',linestyle=':',color='blue',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10)
        plt.plot(x9_ref_RELAP, y9_ref_RELAP,label='bk9_RELAP5',linestyle=':',color='green',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10)
        plt.plot(x_model, y_model_axial_temp_1,label='bk1',color='red',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.plot(x_model, y_model_axial_temp_5,label='bk5',color='blue',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.plot(x_model, y_model_axial_temp_9,label='bk9',color='green',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)
        plt.xlabel('Time (h)')
        plt.ylabel('Temperature (K)')
        plt.title('Axial heating block outer temperature comparison')
        plt.legend(shadow=True, frameon=True,loc='best',fontsize=6,)
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def axial_side_in(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30):
        x1_ref = self.ref_bk1_side_in.iloc[0:,0] 
        y1_ref = self.ref_bk1_side_in.iloc[0:,1]
        x5_ref = self.ref_bk5_side_in.iloc[0:,0]
        y5_ref = self.ref_bk5_side_in.iloc[0:,1]
        x9_ref = self.ref_bk9_side_in.iloc[0:,0]    
        y9_ref = self.ref_bk9_side_in.iloc[0:,1]

        x1_ref_RELAP = self.ref_bk1_side_in_RELAP.iloc[0:,0] 
        y1_ref_RELAP = self.ref_bk1_side_in_RELAP.iloc[0:,1]
        x5_ref_RELAP = self.ref_bk5_side_in_RELAP.iloc[0:,0]
        y5_ref_RELAP = self.ref_bk5_side_in_RELAP.iloc[0:,1]
        x9_ref_RELAP = self.ref_bk9_side_in_RELAP.iloc[0:,0]    
        y9_ref_RELAP = self.ref_bk9_side_in_RELAP.iloc[0:,1]

        x_model = self.selected_data[a]/3600    
        y1_model = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10])/10
        y5_model = (self.selected_data[b11] + self.selected_data[b12] + self.selected_data[b13] + self.selected_data[b14] + self.selected_data[b15] + self.selected_data[b16] + self.selected_data[b17] + self.selected_data[b18] + self.selected_data[b19] + self.selected_data[b20])/10
        y9_model = (self.selected_data[b21] + self.selected_data[b22] + self.selected_data[b23] + self.selected_data[b24] + self.selected_data[b25] + self.selected_data[b26] + self.selected_data[b27] + self.selected_data[b28] + self.selected_data[b29] + self.selected_data[b30])/10
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.figure(figsize=(7,10))
        plt.plot(x1_ref, y1_ref,label='bk1_SAM',linestyle='--',color='red')
        plt.plot(x5_ref, y5_ref,label='bk5_SAM',linestyle='--',color='blue')  
        plt.plot(x9_ref, y9_ref,label='bk9_SAM',linestyle='--',color='green')   
        plt.plot(x1_ref_RELAP, y1_ref_RELAP,label='bk1_RELAP5',linestyle=':',color='red')
        plt.plot(x5_ref_RELAP, y5_ref_RELAP,label='bk5_RELAP5',linestyle=':',color='blue')  
        plt.plot(x9_ref_RELAP, y9_ref_RELAP,label='bk9_RELAP5',linestyle=':',color='green')      
        plt.plot(x_model, y1_model,label='bk1_side_in',color='red',linewidth=2)    
        plt.plot(x_model, y5_model,label='bk5_side_in',color='blue',linewidth=2)    
        plt.plot(x_model, y9_model,label='bk9_side_in',color='green',linewidth=2)    
        plt.xlabel('Time (h)')
        plt.ylabel('Temperature (K)')
        plt.title('Axial side_in reflector temperature comparison')
        plt.legend(shadow=True, frameon=True, fontsize=6, loc='best')
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def axial_side_out(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30):
        x1_ref = self.ref_bk1_side_out.iloc[0:,0] 
        y1_ref = self.ref_bk1_side_out.iloc[0:,1]
        x5_ref = self.ref_bk5_side_out.iloc[0:,0]
        y5_ref = self.ref_bk5_side_out.iloc[0:,1]
        x9_ref = self.ref_bk9_side_out.iloc[0:,0]    
        y9_ref = self.ref_bk9_side_out.iloc[0:,1]   

        x1_ref_RELAP = self.ref_bk1_side_out_RELAP.iloc[0:,0] 
        y1_ref_RELAP = self.ref_bk1_side_out_RELAP.iloc[0:,1]
        x5_ref_RELAP = self.ref_bk5_side_out_RELAP.iloc[0:,0]
        y5_ref_RELAP = self.ref_bk5_side_out_RELAP.iloc[0:,1]
        x9_ref_RELAP = self.ref_bk9_side_out_RELAP.iloc[0:,0]    
        y9_ref_RELAP = self.ref_bk9_side_out_RELAP.iloc[0:,1]  

        x_model = self.selected_data[a]/3600    
        y1_model = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10])/10
        y5_model = (self.selected_data[b11] + self.selected_data[b12] + self.selected_data[b13] + self.selected_data[b14] + self.selected_data[b15] + self.selected_data[b16] + self.selected_data[b17] + self.selected_data[b18] + self.selected_data[b19] + self.selected_data[b20])/10
        y9_model = (self.selected_data[b21] + self.selected_data[b22] + self.selected_data[b23] + self.selected_data[b24] + self.selected_data[b25] + self.selected_data[b26] + self.selected_data[b27] + self.selected_data[b28] + self.selected_data[b29] + self.selected_data[b30])/10
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.figure(figsize=(7,10))
        plt.plot(x1_ref, y1_ref,label='bk1_SAM',linestyle='--',color='red')
        plt.plot(x5_ref, y5_ref,label='bk5_SAM',linestyle='--',color='blue') 
        plt.plot(x9_ref, y9_ref,label='bk9_SAM',linestyle='--',color='green') 
        plt.plot(x1_ref_RELAP, y1_ref_RELAP,label='bk1_RELAP5',linestyle=':',color='red')
        plt.plot(x5_ref_RELAP, y5_ref_RELAP,label='bk5_RELAP5',linestyle=':',color='blue')  
        plt.plot(x9_ref_RELAP, y9_ref_RELAP,label='bk9_RELAP5',linestyle=':',color='green')      
        plt.plot(x_model, y1_model,label='bk1_side_out',color='red',linewidth=2)    
        plt.plot(x_model, y5_model,label='bk5_side_out',color='blue',linewidth=2)    
        plt.plot(x_model, y9_model,label='bk9_side_out',color='green',linewidth=2)    
        plt.xlabel('Time (h)')
        plt.ylabel('Temperature (K)')
        plt.title('Axial side_out reflector temperature comparison')
        plt.legend(shadow=True, frameon=True, fontsize=6, loc='best')
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def axial_per(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30):
        x1_ref = self.ref_bk1_per.iloc[0:,0] 
        y1_ref = self.ref_bk1_per.iloc[0:,1]
        x5_ref = self.ref_bk5_per.iloc[0:,0]
        y5_ref = self.ref_bk5_per.iloc[0:,1]
        x9_ref = self.ref_bk9_per.iloc[0:,0]    
        y9_ref = self.ref_bk9_per.iloc[0:,1]   

        x1_ref_RELAP = self.ref_bk1_per_RELAP.iloc[0:,0] 
        y1_ref_RELAP = self.ref_bk1_per_RELAP.iloc[0:,1]
        x5_ref_RELAP = self.ref_bk5_per_RELAP.iloc[0:,0]
        y5_ref_RELAP = self.ref_bk5_per_RELAP.iloc[0:,1]
        x9_ref_RELAP = self.ref_bk9_per_RELAP.iloc[0:,0]    
        y9_ref_RELAP = self.ref_bk9_per_RELAP.iloc[0:,1]  

        x_model = self.selected_data[a]/3600    
        y1_model = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10])/10
        y5_model = (self.selected_data[b11] + self.selected_data[b12] + self.selected_data[b13] + self.selected_data[b14] + self.selected_data[b15] + self.selected_data[b16] + self.selected_data[b17] + self.selected_data[b18] + self.selected_data[b19] + self.selected_data[b20])/10
        y9_model = (self.selected_data[b21] + self.selected_data[b22] + self.selected_data[b23] + self.selected_data[b24] + self.selected_data[b25] + self.selected_data[b26] + self.selected_data[b27] + self.selected_data[b28] + self.selected_data[b29] + self.selected_data[b30])/10
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.figure(figsize=(7,10))
        plt.plot(x1_ref, y1_ref,label='bk1_SAM',linestyle='--',color='red',marker='v', markersize=5, markevery=len(x1_ref)//10)
        plt.plot(x5_ref, y5_ref,label='bk5_SAM',linestyle='--',color='blue',marker='v', markersize=5, markevery=len(x1_ref)//10)  
        plt.plot(x9_ref, y9_ref,label='bk9_SAM',linestyle='--',color='green',marker='v', markersize=5, markevery=len(x1_ref)//10) 
        plt.plot(x1_ref_RELAP, y1_ref_RELAP,label='bk1_RELAP5',linestyle=':',color='red',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10)
        plt.plot(x5_ref_RELAP, y5_ref_RELAP,label='bk5_RELAP5',linestyle=':',color='blue',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//9)  
        plt.plot(x9_ref_RELAP, y9_ref_RELAP,label='bk9_RELAP5',linestyle=':',color='green',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10) 
        plt.plot(x_model, y1_model,label='bk1_permanent',color='red',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.plot(x_model, y5_model,label='bk5_permanent',color='blue',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.plot(x_model, y9_model,label='bk9_permanent',color='green',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.xlabel('Time (h)')
        plt.ylabel('Temperature (K)')
        plt.title('Axial permanent reflector temperature comparison')
        plt.legend(shadow=True, frameon=True, fontsize=6, loc='best')
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def axial_corebarrel(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30):
        x1_ref = self.ref_bk1_corebarrel.iloc[0:,0] 
        y1_ref = self.ref_bk1_corebarrel.iloc[0:,1]
        x5_ref = self.ref_bk5_corebarrel.iloc[0:,0]
        y5_ref = self.ref_bk5_corebarrel.iloc[0:,1]
        x9_ref = self.ref_bk9_corebarrel.iloc[0:,0]    
        y9_ref = self.ref_bk9_corebarrel.iloc[0:,1]   

        x1_ref_RELAP = self.ref_bk1_corebarrel_RELAP.iloc[0:,0] 
        y1_ref_RELAP = self.ref_bk1_corebarrel_RELAP.iloc[0:,1]
        x5_ref_RELAP = self.ref_bk5_corebarrel_RELAP.iloc[0:,0]
        y5_ref_RELAP = self.ref_bk5_corebarrel_RELAP.iloc[0:,1]
        x9_ref_RELAP = self.ref_bk9_corebarrel_RELAP.iloc[0:,0]    
        y9_ref_RELAP = self.ref_bk9_corebarrel_RELAP.iloc[0:,1] 

        x_model = self.selected_data[a]/3600    
        y1_model = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10])/10
        y5_model = (self.selected_data[b11] + self.selected_data[b12] + self.selected_data[b13] + self.selected_data[b14] + self.selected_data[b15] + self.selected_data[b16] + self.selected_data[b17] + self.selected_data[b18] + self.selected_data[b19] + self.selected_data[b20])/10
        y9_model = (self.selected_data[b21] + self.selected_data[b22] + self.selected_data[b23] + self.selected_data[b24] + self.selected_data[b25] + self.selected_data[b26] + self.selected_data[b27] + self.selected_data[b28] + self.selected_data[b29] + self.selected_data[b30])/10
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.figure(figsize=(7,10))
        plt.plot(x1_ref, y1_ref,label='bk1_SAM',linestyle='--',color='red',marker='v', markersize=5, markevery=len(x1_ref)//10)
        plt.plot(x5_ref, y5_ref,label='bk5_SAM',linestyle='--',color='blue',marker='v', markersize=5, markevery=len(x1_ref)//10)   
        plt.plot(x9_ref, y9_ref,label='bk9_SAM',linestyle='--',color='green',marker='v', markersize=5, markevery=len(x1_ref)//10)    
        plt.plot(x1_ref_RELAP, y1_ref_RELAP,label='bk1_RELAP5',linestyle=':',color='red',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10)    
        plt.plot(x5_ref_RELAP, y5_ref_RELAP,label='bk5_RELAP5',linestyle=':',color='blue',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10)      
        plt.plot(x9_ref_RELAP, y9_ref_RELAP,label='bk9_RELAP5',linestyle=':',color='green',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10) 
        plt.plot(x_model, y1_model,label='bk1_corebarrel',color='red',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.plot(x_model, y5_model,label='bk5_corebarrel',color='blue',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.plot(x_model, y9_model,label='bk9_corebarrel',color='green',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.xlabel('Time (h)')
        plt.ylabel('Temperature (K)')
        plt.title('Axial CoreBarrel temperature comparison')
        plt.legend(shadow=True, frameon=True, fontsize=6, loc='best')
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def axial_vessel(self,a,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30):
        x1_ref = self.ref_bk1_vessel.iloc[0:,0] 
        y1_ref = self.ref_bk1_vessel.iloc[0:,1]
        x5_ref = self.ref_bk5_vessel.iloc[0:,0]
        y5_ref = self.ref_bk5_vessel.iloc[0:,1]
        x9_ref = self.ref_bk9_vessel.iloc[0:,0]    
        y9_ref = self.ref_bk9_vessel.iloc[0:,1]   

        x1_ref_RELAP = self.ref_bk1_vessel_RELAP.iloc[0:,0] 
        y1_ref_RELAP = self.ref_bk1_vessel_RELAP.iloc[0:,1]
        x5_ref_RELAP = self.ref_bk5_vessel_RELAP.iloc[0:,0]
        y5_ref_RELAP = self.ref_bk5_vessel_RELAP.iloc[0:,1]
        x9_ref_RELAP = self.ref_bk9_vessel_RELAP.iloc[0:,0]    
        y9_ref_RELAP = self.ref_bk9_vessel_RELAP.iloc[0:,1]  

        x_model = self.selected_data[a]/3600    
        y1_model = (self.selected_data[b1] + self.selected_data[b2] + self.selected_data[b3] + self.selected_data[b4] + self.selected_data[b5] + self.selected_data[b6] + self.selected_data[b7] + self.selected_data[b8] + self.selected_data[b9] + self.selected_data[b10])/10
        y5_model = (self.selected_data[b11] + self.selected_data[b12] + self.selected_data[b13] + self.selected_data[b14] + self.selected_data[b15] + self.selected_data[b16] + self.selected_data[b17] + self.selected_data[b18] + self.selected_data[b19] + self.selected_data[b20])/10
        y9_model = (self.selected_data[b21] + self.selected_data[b22] + self.selected_data[b23] + self.selected_data[b24] + self.selected_data[b25] + self.selected_data[b26] + self.selected_data[b27] + self.selected_data[b28] + self.selected_data[b29] + self.selected_data[b30])/10
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.figure(figsize=(7,10))
        plt.plot(x1_ref, y1_ref,label='bk1_SAM',linestyle='--',color='red',marker='v', markersize=5, markevery=len(x1_ref)//10)
        plt.plot(x5_ref, y5_ref,label='bk5_SAM',linestyle='--',color='blue',marker='v', markersize=5, markevery=len(x1_ref)//10) 
        plt.plot(x9_ref, y9_ref,label='bk9_SAM',linestyle='--',color='green',marker='v', markersize=5, markevery=len(x1_ref)//10)    
        plt.plot(x1_ref_RELAP, y1_ref_RELAP,label='bk1_RELAP5',linestyle=':',color='red',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10)    
        plt.plot(x5_ref_RELAP, y5_ref_RELAP,label='bk5_RELAP5',linestyle=':',color='blue',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10)      
        plt.plot(x9_ref_RELAP, y9_ref_RELAP,label='bk9_RELAP5',linestyle=':',color='green',marker='^', markersize=5, markevery=len(x1_ref_RELAP)//10) 
        plt.plot(x_model, y1_model,label='bk1_vessel',color='red',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.plot(x_model, y5_model,label='bk5_vessel',color='blue',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.plot(x_model, y9_model,label='bk9_vessel',color='green',linewidth=2,marker='o', markersize=5, markevery=len(x_model)//10)    
        plt.xlabel('Time (h)')
        plt.ylabel('Temperature (K)')
        plt.title('Axial Vessel temperature comparison')
        plt.legend(shadow=True, frameon=True, fontsize=4, loc='lower right',markerscale=0.5)
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()

    def ref_file_steady(self,file_paths_1,file_paths_5,file_paths_9):
        self.ref_data_steady = pd.read_csv(file_paths_1)
        self.ref_data_steady_5 = pd.read_csv(file_paths_5)
        self.ref_data_steady_9 = pd.read_csv(file_paths_9)

    def steady_model(self,file_paths_1,file_paths_5,file_paths_9):
        self.steady_data = pd.read_csv(file_paths_1) 
        self.steady_data_5 = pd.read_csv(file_paths_5)
        self.steady_data_9 = pd.read_csv(file_paths_9)

    def plot_steady_model(self):
        x_model_1 = self.steady_data.iloc[:,0]
        y_model_1 = self.steady_data.iloc[:,1]
        x_ref_1 = self.ref_data_steady.iloc[:,0]
        y_ref_1 = self.ref_data_steady.iloc[:,1]
        x_model_5 = self.steady_data_5.iloc[:,0]
        y_model_5 = self.steady_data_5.iloc[:,1]
        x_ref_5 = self.ref_data_steady_5.iloc[:,0]
        y_ref_5 = self.ref_data_steady_5.iloc[:,1]
        x_model_9 = self.steady_data_9.iloc[:,0]
        y_model_9 = self.steady_data_9.iloc[:,1]
        x_ref_9 = self.ref_data_steady_9.iloc[:,0]
        y_ref_9 = self.ref_data_steady_9.iloc[:,1]
        plt.rcParams.update({
            'font.family': 'serif',        # 使用衬线字体 (学术论文常用)
            'font.serif': ['Times New Roman'],  # 指定Times New Roman
            'mathtext.fontset': 'stix',    # 数学字体与正文一致
            'font.size': 12,               # 基础字号
            'axes.labelsize': 14,          # 坐标轴标签字号
            'axes.linewidth': 1.2,         # 坐标轴线宽
            'legend.fontsize': 4,         # 图例字号
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
        plt.plot(x_model_1, y_model_1,label='bk1-RETA',color='red',linestyle='-')
        plt.plot(x_ref_1, y_ref_1,label='bk1-SAM',linestyle='--',color='red')
        plt.plot(x_model_5, y_model_5,label='bk5-RETA',color='orange',linestyle='-')
        plt.plot(x_ref_5, y_ref_5,label='bk5-SAM',linestyle='--',color='orange')
        plt.plot(x_model_9, y_model_9,label='bk9-RETA',color='blue',linestyle='-')
        plt.plot(x_ref_9, y_ref_9,label='bk9-SAM',linestyle='--',color='blue')
        plt.xlabel('r(m)')  
        plt.ylabel('Temperature (K)')
        plt.title('Steady state temperature comparison')
        plt.legend(shadow=True, frameon=True,framealpha=0.9, fontsize=8, loc='upper right',borderpad=1.2)
        plt.grid(True, linestyle='--', alpha=0.3, linewidth=0.8)
        plt.show()


compare = csvplot()
compare.ref_file_read('F:\资料\高温气冷堆\瞬态数据\central.csv','F:\资料\高温气冷堆\瞬态数据\inner.csv','F:\资料\高温气冷堆\瞬态数据\middle.csv','F:\资料\高温气冷堆\瞬态数据\outer.csv','F:\资料\高温气冷堆\瞬态数据\side.csv','F:\资料\高温气冷堆\瞬态数据\Decay_heat.csv','F:\资料\高温气冷堆\瞬态数据\RCCS.csv','F:\资料\高温气冷堆\瞬态数据\\radial_temp_central.csv','F:\资料\高温气冷堆\瞬态数据\\radial_temp_core.csv','F:\资料\高温气冷堆\瞬态数据\\radial_temp_side.csv','F:\资料\高温气冷堆\瞬态数据\\radial_temp_permanent.csv','D:\Python\HTTF瞬态结果\\bk1_heat_outer.csv','D:\Python\HTTF瞬态结果\\bk5_heat_outer.csv','D:\Python\HTTF瞬态结果\\bk9_heat_outer.csv','D:\Python\HTTF瞬态结果\\bk1_side_in.csv','D:\Python\HTTF瞬态结果\\bk5_side_in.csv','D:\Python\HTTF瞬态结果\\bk9_side_in.csv','D:\Python\HTTF瞬态结果\\bk1_side_out.csv','D:\Python\HTTF瞬态结果\\bk5_side_out.csv','D:\Python\HTTF瞬态结果\\bk9_side_out.csv','D:\Python\HTTF瞬态结果\\bk1_per.csv','D:\Python\HTTF瞬态结果\\bk5_per.csv','D:\Python\HTTF瞬态结果\\bk9_per.csv','D:\Python\HTTF瞬态结果\\bk1_vessel.csv','D:\Python\HTTF瞬态结果\\bk5_vessel.csv','D:\Python\HTTF瞬态结果\\bk9_vessel.csv','D:\Python\HTTF瞬态结果\\bk1_corebarrel.csv','D:\Python\HTTF瞬态结果\\bk5_corebarrel.csv','D:\Python\HTTF瞬态结果\\bk9_corebarrel.csv','D:\Python\HTTF瞬态结果\\bk1_heat_middle.csv','D:\Python\HTTF瞬态结果\\bk5_heat_middle.csv','D:\Python\HTTF瞬态结果\\bk9_heat_middle.csv','D:\Python\HTTF瞬态结果\\bk1_heat_inner.csv','D:\Python\HTTF瞬态结果\\bk5_heat_inner.csv','D:\Python\HTTF瞬态结果\\bk9_heat_inner.csv','D:\Python\HTTF瞬态结果\\bk1_center_in.csv','D:\Python\HTTF瞬态结果\\bk5_center_in.csv','D:\Python\HTTF瞬态结果\\bk9_center_in.csv','D:\Python\HTTF瞬态结果\\bk1_center_out.csv','D:\Python\HTTF瞬态结果\\bk5_center_out.csv','D:\Python\HTTF瞬态结果\\bk9_center_out.csv','D:\Python\HTTF瞬态结果\\bk1_heat_outer_RELAP.csv','D:\Python\HTTF瞬态结果\\bk5_heat_outer_RELAP.csv','D:\Python\HTTF瞬态结果\\bk9_heat_outer_RELAP.csv','D:\Python\HTTF瞬态结果\\bk1_side_in_RELAP.csv','D:\Python\HTTF瞬态结果\\bk5_side_in_RELAP.csv','D:\Python\HTTF瞬态结果\\bk9_side_in_RELAP.csv','D:\Python\HTTF瞬态结果\\bk1_side_out_RELAP.csv','D:\Python\HTTF瞬态结果\\bk5_side_out_RELAP.csv','D:\Python\HTTF瞬态结果\\bk9_side_out_RELAP.csv','D:\Python\HTTF瞬态结果\\bk1_per_RELAP.csv','D:\Python\HTTF瞬态结果\\bk5_per_RELAP.csv','D:\Python\HTTF瞬态结果\\bk9_per_RELAP.csv','D:\Python\HTTF瞬态结果\\bk1_vessel_RELAP.csv','D:\Python\HTTF瞬态结果\\bk5_vessel_RELAP.csv','D:\Python\HTTF瞬态结果\\bk9_vessel_RELAP.csv','D:\Python\HTTF瞬态结果\\bk1_corebarrel_RELAP.csv','D:\Python\HTTF瞬态结果\\bk5_corebarrel_RELAP.csv','D:\Python\HTTF瞬态结果\\bk9_corebarrel_RELAP.csv','D:\Python\HTTF瞬态结果\\bk1_heat_middle_RELAP.csv','D:\Python\HTTF瞬态结果\\bk5_heat_middle_RELAP.csv','D:\Python\HTTF瞬态结果\\bk9_heat_middle_RELAP.csv','D:\Python\HTTF瞬态结果\\bk1_heat_inner_RELAP.csv','D:\Python\HTTF瞬态结果\\bk5_heat_inner_RELAP.csv','D:\Python\HTTF瞬态结果\\bk9_heat_inner_RELAP.csv','D:\Python\HTTF瞬态结果\\bk1_center_in_RELAP.csv','D:\Python\HTTF瞬态结果\\bk5_center_in_RELAP.csv','D:\Python\HTTF瞬态结果\\bk9_center_in_RELAP.csv','D:\Python\HTTF瞬态结果\\bk1_center_out_RELAP.csv','D:\Python\HTTF瞬态结果\\bk5_center_out_RELAP.csv','D:\Python\HTTF瞬态结果\\bk9_center_out_RELAP.csv')

compare.model_file_read('I:\home\huyu\RETA\ML\HTTF_SAMall_trans9.csv')

compare.flow_compare('time','cooled_center_low:outlet:mass','cooled_1_low:outlet:mass','cooled_2_low:outlet:mass','cooled_3_low:outlet:mass','cooled_4_low:outlet:mass','cooled_5_low:outlet:mass','cooled_6_low:outlet:mass','cooled_7_low:outlet:mass','cooled_8_low:outlet:mass','cooled_9_low:outlet:mass','cooled_10_low:outlet:mass','cooled_11_low:outlet:mass','cooled_side_low:outlet:mass')

#compare.power_compare('time','heating_rod1:Qtot','heating_rod2:Qtot','heating_rod3:Qtot','heating_rod4:Qtot','heating_rod5:Qtot','heating_rod6:Qtot','heating_rod7:Qtot','heating_rod8:Qtot','heating_rod9:Qtot','heating_rod10:Qtot','RCCS_outlet:enthalpy','RCCS_inlet:enthalpy')

#compare.radial_block1_temp_compare('time','ceram_center_in:Ts0','ceram_center_in:Ts10','ceram_center_in:Ts20','ceram_center_in:Ts30','ceram_center_in:Ts40','ceram_center_in:Ts50','ceram_center_in:Ts60','ceram_center_in:Ts70','ceram_center_in:Ts80','ceram_center_in:Ts90','ceram_center_out:Ts0','ceram_center_out:Ts10','ceram_center_out:Ts20','ceram_center_out:Ts30','ceram_center_out:Ts40','ceram_center_out:Ts50','ceram_center_out:Ts60','ceram_center_out:Ts70','ceram_center_out:Ts80','ceram_center_out:Ts90','ceram_1_in:Ts0','ceram_1_in:Ts10','ceram_1_in:Ts20','ceram_1_in:Ts30','ceram_1_in:Ts40','ceram_1_in:Ts50','ceram_1_in:Ts60','ceram_1_in:Ts70','ceram_1_in:Ts80','ceram_1_in:Ts90','ceram_1_out:Ts0','ceram_1_out:Ts10','ceram_1_out:Ts20','ceram_1_out:Ts30','ceram_1_out:Ts40','ceram_1_out:Ts50','ceram_1_out:Ts60','ceram_1_out:Ts70','ceram_1_out:Ts80','ceram_1_out:Ts90','ceram_2_in:Ts0','ceram_2_in:Ts10','ceram_2_in:Ts20','ceram_2_in:Ts30','ceram_2_in:Ts40','ceram_2_in:Ts50','ceram_2_in:Ts60','ceram_2_in:Ts70','ceram_2_in:Ts80','ceram_2_in:Ts90','ceram_2_out:Ts0','ceram_2_out:Ts10','ceram_2_out:Ts20','ceram_2_out:Ts30','ceram_2_out:Ts40','ceram_2_out:Ts50','ceram_2_out:Ts60','ceram_2_out:Ts70','ceram_2_out:Ts80','ceram_2_out:Ts90','ceram_3_in:Ts0','ceram_3_in:Ts10','ceram_3_in:Ts20','ceram_3_in:Ts30','ceram_3_in:Ts40','ceram_3_in:Ts50','ceram_3_in:Ts60','ceram_3_in:Ts70','ceram_3_in:Ts80','ceram_3_in:Ts90','ceram_3_out:Ts0','ceram_3_out:Ts10','ceram_3_out:Ts20','ceram_3_out:Ts30','ceram_3_out:Ts40','ceram_3_out:Ts50','ceram_3_out:Ts60','ceram_3_out:Ts70','ceram_3_out:Ts80','ceram_3_out:Ts90','ceram_4_in:Ts0','ceram_4_in:Ts10','ceram_4_in:Ts20','ceram_4_in:Ts30','ceram_4_in:Ts40','ceram_4_in:Ts50','ceram_4_in:Ts60','ceram_4_in:Ts70','ceram_4_in:Ts80','ceram_4_in:Ts90','ceram_4_out:Ts0','ceram_4_out:Ts10','ceram_4_out:Ts20','ceram_4_out:Ts30','ceram_4_out:Ts40','ceram_4_out:Ts50','ceram_4_out:Ts60','ceram_4_out:Ts70','ceram_4_out:Ts80','ceram_4_out:Ts90','ceram_5_in:Ts0','ceram_5_in:Ts10','ceram_5_in:Ts20','ceram_5_in:Ts30','ceram_5_in:Ts40','ceram_5_in:Ts50','ceram_5_in:Ts60','ceram_5_in:Ts70','ceram_5_in:Ts80','ceram_5_in:Ts90','ceram_5_out:Ts0','ceram_5_out:Ts10','ceram_5_out:Ts20','ceram_5_out:Ts30','ceram_5_out:Ts40','ceram_5_out:Ts50','ceram_5_out:Ts60','ceram_5_out:Ts70','ceram_5_out:Ts80','ceram_5_out:Ts90','ceram_6_in:Ts0','ceram_6_in:Ts10','ceram_6_in:Ts20','ceram_6_in:Ts30','ceram_6_in:Ts40','ceram_6_in:Ts50','ceram_6_in:Ts60','ceram_6_in:Ts70','ceram_6_in:Ts80','ceram_6_in:Ts90','ceram_6_out:Ts0','ceram_6_out:Ts10','ceram_6_out:Ts20','ceram_6_out:Ts30','ceram_6_out:Ts40','ceram_6_out:Ts50','ceram_6_out:Ts60','ceram_6_out:Ts70','ceram_6_out:Ts80','ceram_6_out:Ts90','ceram_7_in:Ts0','ceram_7_in:Ts10','ceram_7_in:Ts20','ceram_7_in:Ts30','ceram_7_in:Ts40','ceram_7_in:Ts50','ceram_7_in:Ts60','ceram_7_in:Ts70','ceram_7_in:Ts80','ceram_7_in:Ts90','ceram_7_out:Ts0','ceram_7_out:Ts10','ceram_7_out:Ts20','ceram_7_out:Ts30','ceram_7_out:Ts40','ceram_7_out:Ts50','ceram_7_out:Ts60','ceram_7_out:Ts70','ceram_7_out:Ts80','ceram_7_out:Ts90','ceram_8_in:Ts0','ceram_8_in:Ts10','ceram_8_in:Ts20','ceram_8_in:Ts30','ceram_8_in:Ts40','ceram_8_in:Ts50','ceram_8_in:Ts60','ceram_8_in:Ts70','ceram_8_in:Ts80','ceram_8_in:Ts90','ceram_8_out:Ts0','ceram_8_out:Ts10','ceram_8_out:Ts20','ceram_8_out:Ts30','ceram_8_out:Ts40','ceram_8_out:Ts50','ceram_8_out:Ts60','ceram_8_out:Ts70','ceram_8_out:Ts80','ceram_8_out:Ts90','ceram_9_in:Ts0','ceram_9_in:Ts10','ceram_9_in:Ts20','ceram_9_in:Ts30','ceram_9_in:Ts40','ceram_9_in:Ts50','ceram_9_in:Ts60','ceram_9_in:Ts70','ceram_9_in:Ts80','ceram_9_in:Ts90','ceram_9_out:Ts0','ceram_9_out:Ts10','ceram_9_out:Ts20','ceram_9_out:Ts30','ceram_9_out:Ts40','ceram_9_out:Ts50','ceram_9_out:Ts60','ceram_9_out:Ts70','ceram_9_out:Ts80','ceram_9_out:Ts90','ceram_10_in:Ts0','ceram_10_in:Ts10','ceram_10_in:Ts20','ceram_10_in:Ts30','ceram_10_in:Ts40','ceram_10_in:Ts50','ceram_10_in:Ts60','ceram_10_in:Ts70','ceram_10_in:Ts80','ceram_10_in:Ts90','ceram_10_out:Ts0','ceram_10_out:Ts10','ceram_10_out:Ts20','ceram_10_out:Ts30','ceram_10_out:Ts40','ceram_10_out:Ts50','ceram_10_out:Ts60','ceram_10_out:Ts70','ceram_10_out:Ts80','ceram_10_out:Ts90','ceram_side_in:Ts0','ceram_side_in:Ts10','ceram_side_in:Ts20','ceram_side_in:Ts30','ceram_side_in:Ts40','ceram_side_in:Ts50','ceram_side_in:Ts60','ceram_side_in:Ts70','ceram_side_in:Ts80','ceram_side_in:Ts90','ceram_side_out:Ts0','ceram_side_out:Ts10','ceram_side_out:Ts20','ceram_side_out:Ts30','ceram_side_out:Ts40','ceram_side_out:Ts50','ceram_side_out:Ts60','ceram_side_out:Ts70','ceram_side_out:Ts80','ceram_side_out:Ts90','ceram_inf:Ts0','ceram_inf:Ts10','ceram_inf:Ts20','ceram_inf:Ts30','ceram_inf:Ts40','ceram_inf:Ts50','ceram_inf:Ts60','ceram_inf:Ts70','ceram_inf:Ts80','ceram_inf:Ts90')

#compare.axial_center_in('time','ceram_center_in:Ts0','ceram_center_in:Ts10','ceram_center_in:Ts20','ceram_center_in:Ts30','ceram_center_in:Ts40','ceram_center_in:Ts50','ceram_center_in:Ts60','ceram_center_in:Ts70','ceram_center_in:Ts80','ceram_center_in:Ts90','ceram_center_in:Ts4','ceram_center_in:Ts14','ceram_center_in:Ts24','ceram_center_in:Ts34','ceram_center_in:Ts44','ceram_center_in:Ts54','ceram_center_in:Ts64','ceram_center_in:Ts74','ceram_center_in:Ts84','ceram_center_in:Ts94','ceram_center_in:Ts8','ceram_center_in:Ts18','ceram_center_in:Ts28','ceram_center_in:Ts38','ceram_center_in:Ts48','ceram_center_in:Ts58','ceram_center_in:Ts68','ceram_center_in:Ts78','ceram_center_in:Ts88','ceram_center_in:Ts98')

#compare.axial_center_out('time','ceram_center_out:Ts0','ceram_center_out:Ts10','ceram_center_out:Ts20','ceram_center_out:Ts30','ceram_center_out:Ts40','ceram_center_out:Ts50','ceram_center_out:Ts60','ceram_center_out:Ts70','ceram_center_out:Ts80','ceram_center_out:Ts90','ceram_center_out:Ts4','ceram_center_out:Ts14','ceram_center_out:Ts24','ceram_center_out:Ts34','ceram_center_out:Ts44','ceram_center_out:Ts54','ceram_center_out:Ts64','ceram_center_out:Ts74','ceram_center_out:Ts84','ceram_center_out:Ts94','ceram_center_out:Ts8','ceram_center_out:Ts18','ceram_center_out:Ts28','ceram_center_out:Ts38','ceram_center_out:Ts48','ceram_center_out:Ts58','ceram_center_out:Ts68','ceram_center_out:Ts78','ceram_center_out:Ts88','ceram_center_out:Ts98')

# compare.axial_heat_inner('time','ceram_1_in:Ts0','ceram_1_in:Ts10','ceram_1_in:Ts20','ceram_1_in:Ts30','ceram_1_in:Ts40','ceram_1_in:Ts50','ceram_1_in:Ts60','ceram_1_in:Ts70','ceram_1_in:Ts80','ceram_1_in:Ts90','ceram_2_in:Ts0','ceram_2_in:Ts10','ceram_2_in:Ts20','ceram_2_in:Ts30','ceram_2_in:Ts40','ceram_2_in:Ts50','ceram_2_in:Ts60','ceram_2_in:Ts70','ceram_2_in:Ts80','ceram_2_in:Ts90','ceram_3_in:Ts0','ceram_3_in:Ts10','ceram_3_in:Ts20','ceram_3_in:Ts30','ceram_3_in:Ts40','ceram_3_in:Ts50','ceram_3_in:Ts60','ceram_3_in:Ts70','ceram_3_in:Ts80','ceram_3_in:Ts90','ceram_1_in:Ts4','ceram_1_in:Ts14','ceram_1_in:Ts24','ceram_1_in:Ts34','ceram_1_in:Ts44','ceram_1_in:Ts54','ceram_1_in:Ts64','ceram_1_in:Ts74','ceram_1_in:Ts84','ceram_1_in:Ts94','ceram_2_in:Ts4','ceram_2_in:Ts14','ceram_2_in:Ts24','ceram_2_in:Ts34','ceram_2_in:Ts44','ceram_2_in:Ts54','ceram_2_in:Ts64','ceram_2_in:Ts74','ceram_2_in:Ts84','ceram_2_in:Ts94','ceram_3_in:Ts4','ceram_3_in:Ts14','ceram_3_in:Ts24','ceram_3_in:Ts34','ceram_3_in:Ts44','ceram_3_in:Ts54','ceram_3_in:Ts64','ceram_3_in:Ts74','ceram_3_in:Ts84','ceram_3_in:Ts94','ceram_1_in:Ts8','ceram_1_in:Ts18','ceram_1_in:Ts28','ceram_1_in:Ts38','ceram_1_in:Ts48','ceram_1_in:Ts58','ceram_1_in:Ts68','ceram_1_in:Ts78','ceram_1_in:Ts88','ceram_1_in:Ts98','ceram_2_in:Ts8','ceram_2_in:Ts18','ceram_2_in:Ts28','ceram_2_in:Ts38','ceram_2_in:Ts48','ceram_2_in:Ts58','ceram_2_in:Ts68','ceram_2_in:Ts78','ceram_2_in:Ts88','ceram_2_in:Ts98','ceram_3_in:Ts8','ceram_3_in:Ts18','ceram_3_in:Ts28','ceram_3_in:Ts38','ceram_3_in:Ts48','ceram_3_in:Ts58','ceram_3_in:Ts68','ceram_3_in:Ts78','ceram_3_in:Ts88','ceram_3_in:Ts98')

# compare.axial_heat_middle('time','ceram_4_in:Ts0','ceram_4_in:Ts10','ceram_4_in:Ts20','ceram_4_in:Ts30','ceram_4_in:Ts40','ceram_4_in:Ts50','ceram_4_in:Ts60','ceram_4_in:Ts70','ceram_4_in:Ts80','ceram_4_in:Ts90','ceram_5_in:Ts0','ceram_5_in:Ts10','ceram_5_in:Ts20','ceram_5_in:Ts30','ceram_5_in:Ts40','ceram_5_in:Ts50','ceram_5_in:Ts60','ceram_5_in:Ts70','ceram_5_in:Ts80','ceram_5_in:Ts90','ceram_6_in:Ts0','ceram_6_in:Ts10','ceram_6_in:Ts20','ceram_6_in:Ts30','ceram_6_in:Ts40','ceram_6_in:Ts50','ceram_6_in:Ts60','ceram_6_in:Ts70','ceram_6_in:Ts80','ceram_6_in:Ts90','ceram_7_in:Ts0','ceram_7_in:Ts10','ceram_7_in:Ts20','ceram_7_in:Ts30','ceram_7_in:Ts40','ceram_7_in:Ts50','ceram_7_in:Ts60','ceram_7_in:Ts70','ceram_7_in:Ts80','ceram_7_in:Ts90','ceram_4_in:Ts4','ceram_4_in:Ts14','ceram_4_in:Ts24','ceram_4_in:Ts34','ceram_4_in:Ts44','ceram_4_in:Ts54','ceram_4_in:Ts64','ceram_4_in:Ts74','ceram_4_in:Ts84','ceram_4_in:Ts94','ceram_5_in:Ts4','ceram_5_in:Ts14','ceram_5_in:Ts24','ceram_5_in:Ts34','ceram_5_in:Ts44','ceram_5_in:Ts54','ceram_5_in:Ts64','ceram_5_in:Ts74','ceram_5_in:Ts84','ceram_5_in:Ts94','ceram_6_in:Ts4','ceram_6_in:Ts14','ceram_6_in:Ts24','ceram_6_in:Ts34','ceram_6_in:Ts44','ceram_6_in:Ts54','ceram_6_in:Ts64','ceram_6_in:Ts74','ceram_6_in:Ts84','ceram_6_in:Ts94','ceram_7_in:Ts4','ceram_7_in:Ts14','ceram_7_in:Ts24','ceram_7_in:Ts34','ceram_7_in:Ts44','ceram_7_in:Ts54','ceram_7_in:Ts64','ceram_7_in:Ts74','ceram_7_in:Ts84','ceram_7_in:Ts94','ceram_4_in:Ts8','ceram_4_in:Ts18','ceram_4_in:Ts28','ceram_4_in:Ts38','ceram_4_in:Ts48','ceram_4_in:Ts58','ceram_4_in:Ts68','ceram_4_in:Ts78','ceram_4_in:Ts88','ceram_4_in:Ts98','ceram_5_in:Ts8','ceram_5_in:Ts18','ceram_5_in:Ts28','ceram_5_in:Ts38','ceram_5_in:Ts48','ceram_5_in:Ts58','ceram_5_in:Ts68','ceram_5_in:Ts78','ceram_5_in:Ts88','ceram_5_in:Ts98','ceram_6_in:Ts8','ceram_6_in:Ts18','ceram_6_in:Ts28','ceram_6_in:Ts38','ceram_6_in:Ts48','ceram_6_in:Ts58','ceram_6_in:Ts68','ceram_6_in:Ts78','ceram_6_in:Ts88','ceram_6_in:Ts98','ceram_7_in:Ts8','ceram_7_in:Ts18','ceram_7_in:Ts28','ceram_7_in:Ts38','ceram_7_in:Ts48','ceram_7_in:Ts58','ceram_7_in:Ts68','ceram_7_in:Ts78','ceram_7_in:Ts88','ceram_7_in:Ts98')

#compare.axial_heat_outer('time','ceram_7_in:Ts0','ceram_7_in:Ts10','ceram_7_in:Ts20','ceram_7_in:Ts30','ceram_7_in:Ts40','ceram_7_in:Ts50','ceram_7_in:Ts60','ceram_7_in:Ts70','ceram_7_in:Ts80','ceram_7_in:Ts90','ceram_8_in:Ts0','ceram_8_in:Ts10','ceram_8_in:Ts20','ceram_8_in:Ts30','ceram_8_in:Ts40','ceram_8_in:Ts50','ceram_8_in:Ts60','ceram_8_in:Ts70','ceram_8_in:Ts80','ceram_8_in:Ts90','ceram_9_in:Ts0','ceram_9_in:Ts10','ceram_9_in:Ts20','ceram_9_in:Ts30','ceram_9_in:Ts40','ceram_9_in:Ts50','ceram_9_in:Ts60','ceram_9_in:Ts70','ceram_9_in:Ts80','ceram_9_in:Ts90','ceram_10_in:Ts0','ceram_10_in:Ts10','ceram_10_in:Ts20','ceram_10_in:Ts30','ceram_10_in:Ts40','ceram_10_in:Ts50','ceram_10_in:Ts60','ceram_10_in:Ts70','ceram_10_in:Ts80','ceram_10_in:Ts90','ceram_7_in:Ts4','ceram_7_in:Ts14','ceram_7_in:Ts24','ceram_7_in:Ts34','ceram_7_in:Ts44','ceram_7_in:Ts54','ceram_7_in:Ts64','ceram_7_in:Ts74','ceram_7_in:Ts84','ceram_7_in:Ts94','ceram_8_in:Ts4','ceram_8_in:Ts14','ceram_8_in:Ts24','ceram_8_in:Ts34','ceram_8_in:Ts44','ceram_8_in:Ts54','ceram_8_in:Ts64','ceram_8_in:Ts74','ceram_8_in:Ts84','ceram_8_in:Ts94','ceram_9_in:Ts4','ceram_9_in:Ts14','ceram_9_in:Ts24','ceram_9_in:Ts34','ceram_9_in:Ts44','ceram_9_in:Ts54','ceram_9_in:Ts64','ceram_9_in:Ts74','ceram_9_in:Ts84','ceram_9_in:Ts94','ceram_10_in:Ts4','ceram_10_in:Ts14','ceram_10_in:Ts24','ceram_10_in:Ts34','ceram_10_in:Ts44','ceram_10_in:Ts54','ceram_10_in:Ts64','ceram_10_in:Ts74','ceram_10_in:Ts84','ceram_10_in:Ts94','ceram_7_in:Ts8','ceram_7_in:Ts18','ceram_7_in:Ts28','ceram_7_in:Ts38','ceram_7_in:Ts48','ceram_7_in:Ts58','ceram_7_in:Ts68','ceram_7_in:Ts78','ceram_7_in:Ts88','ceram_7_in:Ts98','ceram_8_in:Ts8','ceram_8_in:Ts18','ceram_8_in:Ts28','ceram_8_in:Ts38','ceram_8_in:Ts48','ceram_8_in:Ts58','ceram_8_in:Ts68','ceram_8_in:Ts78','ceram_8_in:Ts88','ceram_8_in:Ts98','ceram_9_in:Ts8','ceram_9_in:Ts18','ceram_9_in:Ts28','ceram_9_in:Ts38','ceram_9_in:Ts48','ceram_9_in:Ts58','ceram_9_in:Ts68','ceram_9_in:Ts78','ceram_9_in:Ts88','ceram_9_in:Ts98','ceram_10_in:Ts8','ceram_10_in:Ts18','ceram_10_in:Ts28','ceram_10_in:Ts38','ceram_10_in:Ts48','ceram_10_in:Ts58','ceram_10_in:Ts68','ceram_10_in:Ts78','ceram_10_in:Ts88','ceram_10_in:Ts98')

# compare.axial_side_in('time','ceram_side_in:Ts0','ceram_side_in:Ts10','ceram_side_in:Ts20','ceram_side_in:Ts30','ceram_side_in:Ts40','ceram_side_in:Ts50','ceram_side_in:Ts60','ceram_side_in:Ts70','ceram_side_in:Ts80','ceram_side_in:Ts90','ceram_side_in:Ts4','ceram_side_in:Ts14','ceram_side_in:Ts24','ceram_side_in:Ts34','ceram_side_in:Ts44','ceram_side_in:Ts54','ceram_side_in:Ts64','ceram_side_in:Ts74','ceram_side_in:Ts84','ceram_side_in:Ts94','ceram_side_in:Ts8','ceram_side_in:Ts18','ceram_side_in:Ts28','ceram_side_in:Ts38','ceram_side_in:Ts48','ceram_side_in:Ts58','ceram_side_in:Ts68','ceram_side_in:Ts78','ceram_side_in:Ts88','ceram_side_in:Ts98')

# compare.axial_side_out('time','ceram_side_out:Ts0','ceram_side_out:Ts10','ceram_side_out:Ts20','ceram_side_out:Ts30','ceram_side_out:Ts40','ceram_side_out:Ts50','ceram_side_out:Ts60','ceram_side_out:Ts70','ceram_side_out:Ts80','ceram_side_out:Ts90','ceram_side_out:Ts4','ceram_side_out:Ts14','ceram_side_out:Ts24','ceram_side_out:Ts34','ceram_side_out:Ts44','ceram_side_out:Ts54','ceram_side_out:Ts64','ceram_side_out:Ts74','ceram_side_out:Ts84','ceram_side_out:Ts94','ceram_side_out:Ts8','ceram_side_out:Ts18','ceram_side_out:Ts28','ceram_side_out:Ts38','ceram_side_out:Ts48','ceram_side_out:Ts58','ceram_side_out:Ts68','ceram_side_out:Ts78','ceram_side_out:Ts88','ceram_side_out:Ts98')

#compare.axial_per('time','ceram_inf:Ts0','ceram_inf:Ts10','ceram_inf:Ts20','ceram_inf:Ts30','ceram_inf:Ts40','ceram_inf:Ts50','ceram_inf:Ts60','ceram_inf:Ts70','ceram_inf:Ts80','ceram_inf:Ts90','ceram_inf:Ts4','ceram_inf:Ts14','ceram_inf:Ts24','ceram_inf:Ts34','ceram_inf:Ts44','ceram_inf:Ts54','ceram_inf:Ts64','ceram_inf:Ts74','ceram_inf:Ts84','ceram_inf:Ts94','ceram_inf:Ts8','ceram_inf:Ts18','ceram_inf:Ts28','ceram_inf:Ts38','ceram_inf:Ts48','ceram_inf:Ts58','ceram_inf:Ts68','ceram_inf:Ts78','ceram_inf:Ts88','ceram_inf:Ts98')

#compare.axial_vessel('time','Vessel:Ts0','Vessel:Ts10','Vessel:Ts20','Vessel:Ts30','Vessel:Ts40','Vessel:Ts50','Vessel:Ts60','Vessel:Ts70','Vessel:Ts80','Vessel:Ts90','Vessel:Ts4','Vessel:Ts14','Vessel:Ts24','Vessel:Ts34','Vessel:Ts44','Vessel:Ts54','Vessel:Ts64','Vessel:Ts74','Vessel:Ts84','Vessel:Ts94','Vessel:Ts8','Vessel:Ts18','Vessel:Ts28','Vessel:Ts38','Vessel:Ts48','Vessel:Ts58','Vessel:Ts68','Vessel:Ts78','Vessel:Ts88','Vessel:Ts98')

#compare.axial_corebarrel('time','core_barrel:Ts0','core_barrel:Ts10','core_barrel:Ts20','core_barrel:Ts30','core_barrel:Ts40','core_barrel:Ts50','core_barrel:Ts60','core_barrel:Ts70','core_barrel:Ts80','core_barrel:Ts90','core_barrel:Ts4','core_barrel:Ts14','core_barrel:Ts24','core_barrel:Ts34','core_barrel:Ts44','core_barrel:Ts54','core_barrel:Ts64','core_barrel:Ts74','core_barrel:Ts84','core_barrel:Ts94','core_barrel:Ts8','core_barrel:Ts18','core_barrel:Ts28','core_barrel:Ts38','core_barrel:Ts48','core_barrel:Ts58','core_barrel:Ts68','core_barrel:Ts78','core_barrel:Ts88','core_barrel:Ts98')

# compare.ref_file_steady('D:\Python\HTTF稳态结果\\block1_ceram_ref.csv','D:\Python\HTTF稳态结果\\block5_ceram_ref.csv','D:\Python\HTTF稳态结果\\block9_ceram_ref.csv')
# compare.steady_model('D:\Python\HTTF稳态结果\\bk1_ceram.csv','D:\Python\HTTF稳态结果\\bk5_ceram.csv','D:\Python\HTTF稳态结果\\bk9_ceram.csv')
# compare.plot_steady_model()