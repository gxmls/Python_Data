'''
∙ x : X轴数据，列表或数组，可选
∙ y : Y轴数据，列表或数组
∙ format_string: 控制曲线的格式字符串，可选
∙ **kwargs : 第二组或更多(x,y,format_string)
当绘制多条曲线时，各条曲线的x不能省略
color : 控制颜色, color='green'
linestyle : 线条风格, linestyle='dashed'
marker : 标记风格, marker='o'
markerfacecolor: 标记颜色, markerfacecolor='blue'
markersize : 标记尺寸, markersize=20
'‐' 实线 '‐‐' 破折线 '‐.' 点划线 ':' 虚线 '' ' ' 无线条
'.' 点标记             '1' 下花三角标记     'h' 竖六边形标记
',' 像素标记(极小点)    '2' 上花三角标记     'H' 横六边形标记
'o' 实心圈标记          '3' 左花三角标记     '+' 十字标记
'v' 倒三角标记          '4' 右花三角标记     'x' x标记
'^' 上三角标记          's' 实心方形标记     'D' 菱形标记
'>' 右三角标记          'p' 实心五角标记     'd' 瘦菱形标记
'<' 左三角标记          '*' 星形标记         '|' 垂直线标记
'''
import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

a=np.arange(10)
plt.plot(a,a*1.5,'go-',a,a*2.5,'rx',a,a*3.5,'*',a,a*4.5,'b-.')
plt.show()

