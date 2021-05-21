'''
np.savetxt(frame, array, fmt='%.18e', delimiter=None)
• frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文件
• array : 存入文件的数组
• fmt : 写入文件的格式，例如：%d %.2f %.18e
• delimiter : 分割字符串，默认是任何空格

np.loadtxt(frame, dtype=np.float, delimiter=None， unpack=False)
• frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文件
• dtype : 数据类型，可选
• delimiter : 分割字符串，默认是任何空格
• unpack : 如果True，读入属性将分别写入不同变量

局限性：CSV只能有效存储一维和二维数组，np.savetxt() np.loadtxt()只能有效存取一维和二维数组
'''
import numpy as np
a=np.arange(100,dtype=np.int32).reshape(5,20)
np.savetxt("a.csv",a,'%d',delimiter=',') 
b=np.loadtxt("a.csv",dtype=np.float,delimiter=',')
print(b)
b=b=np.loadtxt("a.csv",dtype=np.int,delimiter=',')
print(b)
