'''
plt.xlabel() 对X轴增加文本标签
plt.ylabel() 对Y轴增加文本标签
plt.title() 对图形整体增加文本标签
plt.text() 在任意位置增加文本
plt.annotate() 在图形中增加带箭头的注解
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
matplotlib.rcParams['font.family']='STSong'
matplotlib.rcParams['font.size']=10
a=np.arange(0.0,5.0,0.02)
plt.subplot(211) #plt.subplot(nrows,ncols,plot_number) 在全局绘图区域中创建一个分区体系，并定位到一个字绘图区域
plt.plot(a,f(a))
plt.subplot(2,1,2)
plt.xlabel('横轴：时间')
plt.ylabel('纵轴：振幅')
plt.title(r'正弦波实例',fontproperties='SimHei',fontsize=10)
plt.annotate(r'$\mu=100$',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.1,width=2))
plt.plot(a,np.cos(2*np.pi*a),'r--') #'r--'红色虚线
plt.show()

