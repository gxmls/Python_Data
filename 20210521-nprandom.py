import numpy as np
from numpy import random
a=np.random.rand(3,4,5) #rand(d0,d1,..,dn):根据d0‐dn创建随机数数组，浮点数，[0,1)，均匀分布
print(a)
a2=np.random.randn(3,4,5) #randn(d0,d1,..,dn):根据d0‐dn创建随机数数组，标准正态分布
print(a2)
a3=np.random.randint(100,200,(3,4)) #randint(low[,high,shape]):根据shape创建随机整数或整数数组，范围是[low, high)
print(a3)
np.random.shuffle(a3) #shuffle(a):根据数组a的第1轴进行随排列，改变数组a
print(a3)
print(np.random.permutation(a3)) #permutation(a):根据数组a的第1轴产生一个新的乱序数组，不改变数组a
print(a3) #a3没有被改变
b=np.random.randint(100,200,(8,))
print(np.random.choice(b,(3,2))) #choice(a[,size,replace,p]):从一维数组a中以概率p抽取元素，形成size形状新数组,replace表示是否可以重用元素，默认为False
print(np.random.choice(b,(3,2),p=b/np.sum(b)))
'''
np.random.uniform(low,high,size): 产生具有均匀分布的数组,low起始值,high结束值,size形状
np.random.normal(loc,scale,size): 产生具有正态分布的数组,loc均值,scale标准差,size形状
np.random.poisson(lam,size): 产生具有泊松分布的数组,lam随机事件发生率,size形状
'''
