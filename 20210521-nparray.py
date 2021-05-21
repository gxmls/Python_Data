import numpy as np
from numpy.core.numerictypes import maximum_sctype
def npSum():
    a=np.array([0,1,2,3,4]) #np.array()生成一个ndarray数组
    b=np.array([9,8,7,6,5])
    c=a**2+b**3
    return c
c=np.array([[0,1,2,3,4],[9,8,7,6,5]])
'''
c=np.array(list/tuple, dtype=np.float32),不指定dtype时，NumPy将根据数据情况关联一个dtype类型
'''
print(npSum()) #np.array()输出成[]形式，元素由空格分割
print("c的维度：{}".format(c.ndim)) #.ndim:秩，即轴的数量或维度的数量
print("c的尺度：{}".format(c.shape)) #.shape:ndarray对象的尺度，对于矩阵，n行m列
print("c元素的个数：{}".format(c.size)) #.size:ndarray对象元素的个数，相当于.shape中n*m的值
print("c元素的类型：{}".format(c.dtype)) #.dtype:ndarray对象的元素类型
print("c元素的大小：{} bytes".format(c.itemsize)) #.itemsize:ndarray对象中每个元素的大小，以字节为单位
list_x=np.array([1,2,3,4]) #从列表类型创建
tuple_x=np.array((1,2,3,4)) #从元组类型创建
mix_x=np.array([[1,2],[3,4],(5,6)]) #从列表和元组混合类型创建
ls_range=np.arange(10) #np.arange(n):类似range(n)函数，返回ndarray类型，元素从0到n‐1
print(ls_range) 
ls_ones=np.ones((2,3,4)) #np.ones(shape):根据shape生成一个全1数组，shape是元组类型
print(ls_ones) #如果不指定dtype=np.int32,结果会输出每个元素为 "1."
ls_zeros=np.zeros((3,6),dtype=np.int32) #np.zeros(shape):根据shape生成一个全0数组，shape是元组类型
print(ls_zeros) 
ls_full=np.full((2,4),5) #np.full(shape,val):根据shape生成一个数组，每个元素值都是val
print(ls_full)
ls_eye=np.eye(5,dtype=np.int32) #np.eye(n):创建一个正方的n*n单位矩阵，对角线为1，其余为0
print(ls_eye) #只有左上到右下的对角线为1
a=np.linspace(1,10,4) #np.linspace(start,stop,num):根据起(start)止(stop)数据等间距地填充num个数据，形成数组
a2=np.linspace(1,10,4,endpoint=False) #np.linspace(start,stop,num,endpoint=True/False):endpoint=False时不包括stop的数据
a3=np.linspace(1,10,4,retstep=True) #np.linspace(start,stop,num,retstep=True/False):retstep=True时，返回数据间的步长
print(a,a2,a3)
b=np.concatenate((a,a2)) #将两个或多个数组合并成一个新的数组,注意是(a,a2)而不是a,a2
print(b)
x=np.arange(24)
print(x.reshape((3,8))) #.reshape(shape):不改变数组元素，返回一个shape形状的数组，原数组不变
print(x) #x没有被.reshape()修改
x.resize((3,8)) #与.reshape()功能一致，但修改原数组
print(x) #使用.resize()后x被修改
print(x.flatten()) #对数组进行降维，返回折叠后的一维数组，原数组不变
print(x) #x没有被.flatten()修改
x=x.astype(np.float) #astype()方法一定会创建新的数组（原始数据的一个拷贝），即使两个类型一致
print(x)
ls=x.tolist() #.tolist():将数组转换成列表
print(ls)
ra=np.arange(24,dtype=np.int32).reshape((2,3,4)) #2个3行4列二维数组组成的数组
print(ra)
print(ra[1,2,3],ra[0,1,2],ra[-1,-2,-3]) #索引：每一个维度上的索引，用逗号分割
print(ra[:,1,-3]) #切片：选取一个维度用":",[:,1,-3]表示每一个维度上的第1行第-3个元素
print(ra[:,1:3,:]) #切片：[:,1:3,:]表示每一个维度上的第1行到第2行的每一个元素
print(ra[:,:,::2]) #切片：[:,:,::2]表示每一个维度上的每一行上的元素从0开始以2为步长切片
ma=ra/ra.mean() #数组与标量之间的运算作用于数组的每一个元素
print(ma)
mb=np.sqrt(ra)
print(np.maximum(ra,mb)) #运算结果为浮点数
print(ra>mb) #运算结果为bool
