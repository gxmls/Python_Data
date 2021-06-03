import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei' #pyplot并不默认支持中文显示，需要rcParams修改字体实现 'SimHei'是黑体
'''
'font.family' 用于显示字体的名字
'font.style' 字体风格，正常'normal'或斜体'italic'
'font.size' 字体大小，整数字号或者'large'、'x‐small'
'''
plt.plot([3,1,4,5,2]) #plt.plot()只有一个输入列表或数组时，参数被当作Y轴，X轴以索引自动生成
plt.ylabel("纵轴(值)")
'''
plt.savefig("test",dpi=600) #plt.savefig()将输出图形存储为文件，默认PNG格式，可以通过dpi修改输出质量
'''
plt.show()

