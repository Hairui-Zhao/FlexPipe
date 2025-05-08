import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np


fig,ax=plt.subplots(1,1, figsize=(4.5,3), dpi=80)
fig.subplots_adjust(left=0.113,right=0.99,top=0.83,bottom=0.20,
                    wspace=0.23,hspace=0.1)
plt.rcParams["font.sans-serif"] = ['Calibri']
plt.rcParams["axes.unicode_minus"] = False

font_legend = {'family': 'Calibri',
         'weight': 'normal',
         'size': 15.2}
ax.set_ylim(0,21000)

x_axis_data = ['512','1024','2048','4096','8192']
#y_axis_data1 =  [4.72, 3.17, 3.26, 2.63, 3.35, 2.3, 2.8, 2.1]
y_axis_data2 = [18956,	18511,	17928,	16721,	15629]
y_axis_data3 = [16800,	15932,	14218,	12134,	10679]
y_axis_data4 = [15551,	14288,	12552,	10781,	8219]
y_axis_data5 = [14721,	12004,	10341,	7511,	4832]
colormap = plt.get_cmap('Blues')

# 获得对应的颜色
# colors   = colormap(range(1, num + 1, 1)) # 0到255
# colors   = colormap(num)
colors= colormap(np.linspace(0.1, 1, 5))
ax.yaxis.get_offset_text().set_fontsize(16)
x_width = np.arange(0, len(x_axis_data))

x1=ax.bar(x_width-0.27 , y_axis_data2, lw=0.5,  edgecolor='white',width=0.18, label="ElaPipe", hatch="///",zorder=0,color=[47/255,45/255,84/255])
x2=ax.bar(x_width-0.09, y_axis_data3, lw=0.5, edgecolor='white',width=0.18, label="DynaPipe", hatch="+++",zorder=0,color=[145/255,147/255,180/255])
x3=ax.bar(x_width+0.09, y_axis_data4, lw=0.5,  width=0.18, edgecolor='white', label=r"Attn Mask",hatch="|||", zorder=0,color=[189/255,154/255,173/255])
x4=ax.bar(x_width+0.27, y_axis_data5, lw=0.5,  width=0.18, edgecolor='white', label=r"Padding", hatch="---",zorder=0,color=[232/255,210/255,179/255])
# ax[0].legend(loc='best')

fig.legend( [x1,x2,x3,x4],['FlexPipe','DynaPipe','FA','ZB'],ncol =4,
             loc = 'upper center',prop = font_legend,frameon =True,bbox_to_anchor=(0.55,1.038),columnspacing=0.6,labelspacing=0.01,handlelength=0.95, handleheight=0.60)

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((0, 0))
ax.yaxis.set_major_formatter(formatter)
ax.yaxis.get_offset_text().set_fontsize(10)
ax.set_xticks(range(0, len(x_axis_data)), x_axis_data)

ax.set_xlabel('Max Sequence Length',fontsize=18)#,labelpad=18
ax.set_ylabel('Throughput (image/s)', fontsize=18)

ax.tick_params(axis='y',
                 labelsize=18, # y轴字体大小设置
                  )
ax.tick_params(axis='x',
                 labelsize=18, # y轴字体大小设置
               )

#ax[0].legend(bbox_to_anchor=(2.71,1.2),ncol=8,fancybox=True,shadow=True,fontsize=20)
ax.grid(None, which='major', axis='both', zorder=0, linestyle='--')

plt.savefig(r".\th_seq_gpt13.pdf")



# plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
