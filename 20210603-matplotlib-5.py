'''
plt.subplot2grid(GridSpec, CurSpec, colspan=1, rowspan=1)
理念：设定网格，选中网格，确定选中行列区域数量，编号从0开始
'''
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
plt.subplot2grid((3,3),(0,0),colspan=3)
plt.plot([3,1,4,5,2])
plt.subplot2grid((3,3),(1,0),colspan=2)
plt.plot([3,1,4,5,2])
plt.subplot2grid((3,3),(1,2),rowspan=2)
plt.plot([3,1,4,5,2])
plt.subplot2grid((3,3),(2,0))
plt.plot([3,1,4,5,2])
plt.subplot2grid((3,3),(2,1))
plt.plot([3,1,4,5,2])
plt.show()
