# -*- cOding: UTF-8 -*-
#列表生成式学习过程
import os
print('生成1，2，3，4，5这样一个列表,可以直接用 list(range(100))')
print(list(range(1,101)))
print('生成1*1，2*2，3*3的list')
L = []
for x in range(1,11):
    L.append(x*x)
print(L)
#第二种方式列表生成式
print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x % 2 == 0])
print([m+n for m in 'abc' for n in 'xyz'])
print([d for d in os.listdir('.')])
print([d for d in os.listdir('.') if d[0] != '.'])#列表非隐藏文件
#竖形列表
for d in os.listdir('.'):
    if d[0] != '.':
        print(d)
    pass
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for m,n in d.items():
    print (m,"=",n)
print([m+"="+n for m,n in d.items()])
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
#这里是列表生成式的课后练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
x = 0
for m in L1:
    if isinstance(m,str):
        L2.append(m)
        x = x + 1
    else:
        print('第',x+1,'个数不是str，所以不记录进入L2，以下显示L2')
        x = x + 1
print([n.lower() for n in L2])
#第二种解法
L2 = [y.lower() for y in L1 if isinstance(y,str)]
print(L2)
