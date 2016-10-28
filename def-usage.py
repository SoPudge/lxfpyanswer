# -*- coding: utf-8 -*-
import math
#用def定义一个绝对值函数
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x
name = input('请输入数值，来计算绝对值：')
print(my_abs(float(name)))#这里float的原因是，input出来的值是str类型，转换成数字
print('求解一元二次方程，a,b,c三个参数：')
def quanratic(a,b,c):
    if b*b - 4*a*c >= 0:
        x1 = (-b + math.sqrt(b*b-4*a*c)) / 2*a
        x2 = (-b - math.sqrt(b*b-4*a*c)) / 2*a
        return x1,x2
    else:
        print('方程无解')
#输入内容求解
canshu = []
n = 0
while n < 3:
    name = input('请输入参数')
    canshu.append(float(name))
    n = n + 1
print(quanratic(canshu[0],canshu[1],canshu[2]))
x = quanratic(10,78,6)
print(x)
#返回多个值的def实际上是一个tuple
