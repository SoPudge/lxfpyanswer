# -*- cOding: UTF-8 -*-
#创建一个generator的方法，把列表生成式中的中括号改为小括号即可
L = (x*x for x in range(10))
print(L)
#可以用循环打印列表生成式
for m in L:
    print(m)
#斐波那契数列使用列表生成式
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        #b = a + b
        #a = b
        a ,b = b, a+b#exchange a and b without temp
        n = n + 1
    return "done"
fib(8)
print("打印斐波那契数列fib(8)")
def fib2(max2):
    if max2 <= 2:
         return 1
    else:
        return fib2(max2-1)+fib2(max2-2)
[print(fib2(x)) for x in range(1,10)]
h = map(fib2,range(1,15))#map定义一个计算方式
print(list(h))
print("打印斐波那契数列fib2(8)")
def fib3(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        #a ,b = b, a+b#等同于下面三句语句
        x = b#首先利用一个辅助x等于b做存储，把前一个b存起来
        b = a + b#然后把第二个b等于前面两个数相加
        a = x#然后把a等于前一个b，循环之后，就是前一个b（a）+后一个b，即fib
        n = n + 1
    return "done"
f = fib3(9)
print("打印yield的fib3，提示是一个生成式",f)
print("用循环打印yield的fib3，提示是一个生成式")
for x in fib3(14):
    print(x)
#生成式作业，打印杨辉三角，实际是yield的使用
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i]+L[i-1] for i in range(len(L))]
#首先附加L增加位数，然后重新定义L，增加位数的L，实际上是上一个列表，后面加0
#此时，只需要江该列表的第一位和第二位相加，就是下一个列表的第二位
#print("print triangles",triangles(9))
def triangles2():
    L = [1]
    while True:
        S = L
        yield L
        L.append(1)
        for t in range(1,len(L)-1):
            L[t]=S[t]+S[t-1]

n = 0
for x in triangles2():
    print(x)
    n = n+1
    if n == 10:
        break
