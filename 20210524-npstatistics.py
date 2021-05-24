import numpy as np
from numpy.core.fromnumeric import argmax
a=np.arange(15).reshape(3,5)
print(a)
print(np.sum(a)) #np.sum(a,axis=None): 根据给定轴axis计算数组a相关元素之和，axis整数或元组
print(np.mean(a,axis=1)) #np.mean(a,axis=None): 根据给定轴axis计算数组a相关元素的期望，axis整数或元组
'''
axis=0时，只对第一维度进行操作，即对三个矩阵[0 1 2 3 4],[5 6 7 8 9]和[10 11 12 13 14]进行操作得到每一列的期望[5. 6. 7. 8. 9.]
axis=1时，对每一个矩阵进行操作，得到每一个矩阵的期望[2. 7. 12.]
axis=None时，计算所有元素的期望得到7.0
'''
print(np.average(a,axis=0,weights=[10,5,1])) #average(a,axis=None,weights=None): 根据给定轴axis计算数组a相关元素的加权平均值
'''
2.1878=(0*10+5*5+10*1)/(10+5+1)
4.1875=(2*10+7*5+1*12*1)/(10+5+1)=4.1875
'''
print(np.std(a)) #std(a,axis=None) 根据给定轴axis计算数组a相关元素的标准差
print(np.var(a)) #var(a,axis=None) 根据给定轴axis计算数组a相关元素的方差
b=np.arange(15,0,-1).reshape(3,5)
print(b)
print(np.min(b),np.max(b)) #np.min(b)/np.max(b): 计算数组b中元素的最小值、最大值
print(np.argmin(b),argmax(b)) #np.argmin(b)/np.argmax(b): 计算数组b中元素最小值、最大值的降一维后下标
'''
降一维只扁平化数组b，比如最小元素1下标为14，最大元素15的下标为0
'''
print(np.unravel_index(np.argmax(b),b.shape)) #np.unravel_index(index,shape): 根据shape将一维下标index转换成多维下标
print(np.ptp(b)) #np.ptp(b): 计算数组b中元素最大值与最小值的差
print(np.median(b)) #np.median(b): 计算数组b中元素的中位数（中值）
f=np.random.randint(0,20,(5))
print(f)
print(np.gradient(f)) #np.gradient(f): 计算数组f中元素的梯度，当f为多维时，返回每个维度梯度
'''
梯度：连续值之间的变化率，即斜率
XY坐标轴连续三个X坐标对应的Y轴值：a, b, c，其中，b的梯度是： (c‐a)/2
'''



