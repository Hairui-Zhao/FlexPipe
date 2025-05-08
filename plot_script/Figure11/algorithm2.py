import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np


fig,ax=plt.subplots(1,1, figsize=(4.5,2.8), dpi=80)
fig.subplots_adjust(left=0.14,right=0.94,top=0.89,bottom=0.15,
                    wspace=0.23,hspace=0.1)
plt.rcParams["font.sans-serif"] = ['Calibri']
plt.rcParams["axes.unicode_minus"] = False
plt.yscale('log')
font_legend = {'family': 'Calibri',
         'weight': 'normal',
         'size': 17,}

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((0, 0))
ax.yaxis.set_major_formatter(formatter)
ax.yaxis.get_offset_text().set_fontsize(10)



x_axis_data = ['BERT24','BERT96','GPT(3.35B)','GPT(13B)']


# 获得对应的颜色
# colors   = colormap(range(1, num + 1, 1)) # 0到255
# colors   = colormap(num)
ax.yaxis.get_offset_text().set_fontsize(16)
x_width = np.arange(0, len(x_axis_data))


# ax[0].legend(loc='best')




ax.yaxis.get_offset_text().set_fontsize(10)
ax.set_xticks(range(0, len(x_axis_data)), x_axis_data)

# ax.set_xlabel('Workloads',fontsize=20)#,labelpad=18
ax.set_ylabel('Throughout (token/s)', fontsize=20)



ax.set_ylim(0,4500)
ax.set_ylabel('Overhead (ms)', fontsize=20)
ax.tick_params(axis='y',labelsize=16)
ax.tick_params(axis='y',
                 labelsize=18, # y轴字体大小设置
                  )
ax.tick_params(axis='x',
                 labelsize=15.7, # y轴字体大小设置
               )

cost1=[3,	15,	17	,25]
cost2=[48,	167,	678	,2087]
x1,=ax.plot(x_axis_data, cost1, 'h--', alpha=0.8, linewidth=2,color=[191/255,29/255,45/255],markersize=10,zorder=7)
x2,=ax.plot(x_axis_data, cost2, 'D--', alpha=0.8, linewidth=2,color=[160/255,100/255,160/255],markersize=10,zorder=7)

fig.legend( [x1,x2],['HBSA','HBSA w/o BD'],ncol =4,
             loc = 'upper center',prop = font_legend,frameon = False,bbox_to_anchor=(0.59,1.05),columnspacing=0.4,labelspacing=0.02
            ,handlelength=1.6, handleheight=0.60)


#ax[0].legend(bbox_to_anchor=(2.71,1.2),ncol=8,fancybox=True,shadow=True,fontsize=20)
ax.grid(None, which='major', axis='both', zorder=0, linestyle='--')

plt.savefig(r".\algorithm2.svg")



# plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
