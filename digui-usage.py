# -*- coding: utf-8 -*-
#递归函数
def fact(n):
    if n == 1:
        return 1
    return n* fact(n-1)
name = int(input('请输入阶乘计算数值：'))
def fact2(n):
    sum = 1
    while n >0:
        sum = sum * n
        n = n-1
    return sum
print(fact(name))
print(fact2(name))
#问题在于fact和fact2，其中fact用迭代完成了fact2循环的内容，明显在方便程度上，迭代优于循环，且迭代更好理解
#python实现汉诺塔问题
#汉诺塔问题是指，把n个原盘，看成最下面的第n个，加上上面的一部分n-1个
#然后每次都是把n移动到缓冲区，再把最下面的移动到终点
def move(n,a,b,c):
    if n == 1:
        print(a,'--->',c)
        return
    else:
        move(n-1,a,c,b)#当有n-1个盘子的时候，我们要把n-1移动到b，再把n移动到c，所以就是a-b的过程，此时c是缓冲区，放在中间
        print('move',a,'--->',c)
        move(n-1,b,a,c)
        return
name = int(input('请输入数字移动次数：'))
move(name,'A','B','C')
