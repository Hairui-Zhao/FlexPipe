import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np


fig,ax=plt.subplots(1,1, figsize=(4.5,2.8), dpi=80)
fig.subplots_adjust(left=0.14,right=0.96,top=0.89,bottom=0.15,
                    wspace=0.23,hspace=0.1)
plt.rcParams["font.sans-serif"] = ['Calibri']
plt.rcParams["axes.unicode_minus"] = False

font_legend = {'family': 'Calibri',
         'weight': 'normal',
         'size': 17,}

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((0, 0))
ax.yaxis.set_major_formatter(formatter)
ax.yaxis.get_offset_text().set_fontsize(10)

ax.set_ylim(0,40000)

x_axis_data = ['BERT24','BERT96','GPT(3.35B)','GPT(13B)']
#y_axis_data1 =  [4.72, 3.17, 3.26, 2.63, 3.35, 2.3, 2.8, 2.1]
y_axis_data2 = [18511,	36443,	26741,	33881]
y_axis_data3 = [13861,	30067,	18953,	25345]
y_axis_data2.reverse()
y_axis_data3.reverse()
colormap = plt.get_cmap('Blues')

# 获得对应的颜色
# colors   = colormap(range(1, num + 1, 1)) # 0到255
# colors   = colormap(num)
colors= colormap(np.linspace(0.1, 1, 5))
ax.yaxis.get_offset_text().set_fontsize(16)
x_width = np.arange(0, len(x_axis_data))

x1=ax.bar(x_width-0.18 , y_axis_data2, lw=0.5,  edgecolor='white',width=0.36, label="ElaPipe", hatch="xxx",zorder=7,color=[56/255,97/255,149/255])
x2=ax.bar(x_width+0.18, y_axis_data3, lw=0.5, edgecolor='white',width=0.36, label="DynaPipe", hatch="///",zorder=7,color=[111/255,185/255,208/255])

# ax[0].legend(loc='best')




ax.yaxis.get_offset_text().set_fontsize(10)
ax.set_xticks(range(0, len(x_axis_data)), x_axis_data)

# ax.set_xlabel('Workloads',fontsize=20)#,labelpad=18
ax.set_ylabel('Throughout (token/s)', fontsize=20)

ax.tick_params(axis='y',
                 labelsize=18, # y轴字体大小设置
                  )
ax.tick_params(axis='x',
                 labelsize=15.7, # y轴字体大小设置
               )




fig.legend( [x1,x2],['FlexPipe','Flex w/o M'],ncol =2,
             loc = 'upper center',prop = font_legend,frameon = False,bbox_to_anchor=(0.59,1.05),columnspacing=0.4,labelspacing=0.02
            ,handlelength=1.6, handleheight=0.60)


#ax[0].legend(bbox_to_anchor=(2.71,1.2),ncol=8,fancybox=True,shadow=True,fontsize=20)
ax.grid(None, which='major', axis='both', zorder=0, linestyle='--')

plt.savefig(r".\algorithm1.pdf")



# plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
