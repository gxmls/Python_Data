'''
plt.subplot2grid(GridSpec, CurSpec, colspan=1, rowspan=1)
理念：设定网格，选中网格，确定选中行列区域数量，编号从0开始
'''
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
gs=gridspec.GridSpec(3,3)
ax1=plt.subplot(gs[0,:])
ax2=plt.subplot(gs[1,:-1])
ax3=plt.subplot(gs[1:,-1])
ax4=plt.subplot(gs[2,0])
ax5=plt.subplot(gs[2,1])
plt.show()
