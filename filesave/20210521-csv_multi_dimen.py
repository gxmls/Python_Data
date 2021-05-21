'''
a.tofile(frame, sep='', format='%s')
• frame : 文件、字符串
• sep : 数据分割字符串，如果是空串，写入文件为二进制
• format : 写入数据的格式

np.fromfile(frame, dtype=float, count=‐1, sep='')
• frame : 文件、字符串
• dtype : 读取的数据类型
• count : 读入元素个数，‐1表示读入整个文件
• sep : 数据分割字符串，如果是空串，写入文件为二进制

该方法需要读取时知道存入文件时数组的维度和元素类型
a.tofile()和np.fromfile()需要配合使用
可以通过元数据文件来存储额外信息

便捷存储：
np.save(fname, array) 或np.savez(fname, array)
• fname : 文件名，以.npy为扩展名，压缩扩展名为.npz
• array : 数组变量
np.load(fname)
• fname : 文件名，以.npy为扩展名，压缩扩展名为.npz
'''

import numpy as np
from numpy.core.records import fromfile
a=np.arange(100,dtype=np.int32).reshape(5,5,4)
a.tofile('F:\\Learning Python\\MOOC_data\\b.dat',sep=',',format='%d')
c=np.fromfile('F:\\Learning Python\\MOOC_data\\b.dat',sep=',',dtype=int).reshape(5,5,4)
print(c)
