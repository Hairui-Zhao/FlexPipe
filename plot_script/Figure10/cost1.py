import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np


fig,ax=plt.subplots(1,1, figsize=(4.5,2.8), dpi=80)
fig.subplots_adjust(left=0.14,right=0.99,top=0.89,bottom=0.15,
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

ax.set_ylim(0,7000)
# plt.yscale('log')
x_axis_data = ['BERT24','BERT96','GPT(3.35B)','GPT(13B)']
#y_axis_data1 =  [4.72, 3.17, 3.26, 2.63, 3.35, 2.3, 2.8, 2.1]
y_axis_data2 = [590,	1740,2840,6501.2]
y_axis_data3 = [562.4,	1464,	2612,6159.2]
y_axis_data4 = [479.6,1442.4,2492,5960]
y_axis_data5 = [360.8,1105.2,2086.4,5414]
colormap = plt.get_cmap('Blues')

# 获得对应的颜色
# colors   = colormap(range(1, num + 1, 1)) # 0到255
# colors   = colormap(num)
colors= colormap(np.linspace(0.1, 1, 5))
ax.yaxis.get_offset_text().set_fontsize(16)
x_width = np.arange(0, len(x_axis_data))


x1=ax.bar(x_width-0.3 , y_axis_data5, lw=0.5,  edgecolor='white',width=0.2, label="ElaPipe",zorder=0,color=[244/255,169/255,155/255])
x2=ax.bar(x_width-0.1, y_axis_data4, lw=0.5, edgecolor='white',width=0.2, label="DynaPipe",zorder=0,color=[153/255,153/255,153/255])
x3=ax.bar(x_width+0.1, y_axis_data3, lw=0.5,  width=0.2, edgecolor='white', label=r"Padding", zorder=0,color=[1/255,144/255,146/255])
x4=ax.bar(x_width+0.3, y_axis_data2, lw=0.5,  width=0.2, edgecolor='white', label=r"Padding", zorder=0,color=[1/255,84/255,147/255])

# ax[0].legend(loc='best')

fig.legend( [x1,x2,x3,x4],['FlexPipe','Flex w/o TL','Ite-Stall','Sus-Res'],ncol =1,
             loc = 'upper right',prop = font_legend,frameon = True,bbox_to_anchor=(0.5438,0.93),columnspacing=0.4,labelspacing=0.05,handlelength=0.95, handleheight=0.60)


ax.yaxis.get_offset_text().set_fontsize(10)
ax.set_xticks(range(0, len(x_axis_data)), x_axis_data)

# ax.set_xlabel('Workloads',fontsize=20)#,labelpad=18
ax.set_ylabel('Training Time (s)', fontsize=20)

ax.tick_params(axis='y',
                 labelsize=17, # y轴字体大小设置
                  )
ax.tick_params(axis='x',
                 labelsize=14.7, # y轴字体大小设置
               )


#ax[0].legend(bbox_to_anchor=(2.71,1.2),ncol=8,fancybox=True,shadow=True,fontsize=20)
# ax.grid(None, which='major', axis='both', zorder=0, linestyle='--')

plt.savefig(r".\cost1.pdf")



# plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
