import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np


fig,ax=plt.subplots(1,1, figsize=(9,2.8), dpi=80)
fig.subplots_adjust(left=0.08,right=0.99,top=0.89,bottom=0.15,
                    wspace=0.23,hspace=0.1)
plt.rcParams["font.sans-serif"] = ['Calibri']
plt.rcParams["axes.unicode_minus"] = False

font_legend = {'family': 'Calibri',
         'weight': 'normal',
         'size': 17,}

ax.set_ylim(0,11)

x_axis_data = ['BERT24','BERT96','GPT(3.35B)','BERT24','BERT96','GPT(3.35B)','BERT24','BERT96','GPT(3.35B)']
#y_axis_data1 =  [4.72, 3.17, 3.26, 2.63, 3.35, 2.3, 2.8, 2.1]
y_axis_data2 = [10	,7.5	,4 ,10,	7.5,	4 ,10,	7.5,	4]
y_axis_data3 = [5.1,	3.2,	1.89 ,4.02,	2.58	,1.23 ,3.55,	2.12,	1]
y_axis_data4 = 	[4.1,	3.02,	1.08, 3.4,	2.15,	0.98 ,3	,1.76	,0.85]
y_axis_data5 = [2.1,	1.02,	0.4 ,1.13,	0.66,	0.28 ,0.98	,0.46	,0.16]
y_axis_data2.reverse()
y_axis_data3.reverse()
y_axis_data4.reverse()
y_axis_data5.reverse()
colormap = plt.get_cmap('Blues')

# 获得对应的颜色
# colors   = colormap(range(1, num + 1, 1)) # 0到255
# colors   = colormap(num)
colors= colormap(np.linspace(0.1, 1, 5))
ax.yaxis.get_offset_text().set_fontsize(16)
x_width = np.arange(0, len(x_axis_data))

x1=ax.bar(x_width-0.3 , y_axis_data5, lw=0.5,  edgecolor='white',width=0.2, label="ElaPipe", hatch="oo",zorder=0,color=[244/255,169/255,155/255])
x2=ax.bar(x_width-0.1, y_axis_data4, lw=0.5, edgecolor='white',width=0.2, label="DynaPipe", hatch="|||",zorder=0,color=[153/255,153/255,153/255])
x3=ax.bar(x_width+0.1, y_axis_data3, lw=0.5,  width=0.2, edgecolor='white', label=r"Padding",hatch="---", zorder=0,color=[1/255,144/255,146/255])
x4=ax.bar(x_width+0.3, y_axis_data2, lw=0.5,  width=0.2, edgecolor='white', label=r"Padding",hatch="xxx", zorder=0,color=[1/255,84/255,147/255])

# ax[0].legend(loc='best')

fig.legend( [x1,x2,x3,x4],['FlexPipe','Flex w/o TL','Ite-Stall','Sus-Res'],ncol =4,
             loc = 'upper center',prop = font_legend,frameon = False,bbox_to_anchor=(0.538,1.05),columnspacing=1,labelspacing=1)

plt.axvline(2.5,color='black',linestyle="--",linewidth=0.85)
plt.axvline(5.5,color='black',linestyle="--",linewidth=0.85)

ax.yaxis.get_offset_text().set_fontsize(10)
ax.set_xticks(range(0, len(x_axis_data)), x_axis_data)
ax.set_yticks([0,2,4,6,8,10])

# ax.set_xlabel('Workloads',fontsize=20)#,labelpad=18
ax.set_ylabel('Overhead (s)', fontsize=20)

ax.tick_params(axis='y',
                 labelsize=17, # y轴字体大小设置
                  )
ax.tick_params(axis='x',
                 labelsize=14.7, # y轴字体大小设置
               )


#ax[0].legend(bbox_to_anchor=(2.71,1.2),ncol=8,fancybox=True,shadow=True,fontsize=20)
# ax.grid(None, which='major', axis='both', zorder=0, linestyle='--')

plt.savefig(r".\cost3.svg",format="svg",dpi=600)



# plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
