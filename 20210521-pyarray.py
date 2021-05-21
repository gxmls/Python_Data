def pySum():
    a=[0,1,2,3,4]
    b=[9,8,7,6,5]
    c=[]
    for i in range(5):
        c.append(a[i]**2+b[i]**3)
    return c
print(pySum()) #输出列表，元素由逗号分割