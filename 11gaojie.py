# -*- coding: utf-8 -*-
from functools import reduce
def add(x,y,f):
    return f(x)+f(y)
print(add(8,100,abs)) 
#map函数的意思，map传入两个参数，一个是函数本身，一个是一个可迭代对象，意思就是将函数作用于可迭代对象，并将结果再次生成一个可迭代对象，放在list内 
#map的意义在于可以定义一个f的方法，然后批量的使用这种方法
def f(x): 
    return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
print('r = map(f,[1,2,3,4,5,6,7,8,9])，结果如下')
print(list(r))
m = map(str,range(10))
print(list(m))
#reduce 函数有两个参数，第一个是函数f，第二个是一个list，意思是将f作用于list中的前两个值，将计算的结果和第三个值，组成两个值，在用f来计算，依次类推
def add(x,y):
    return x + y
print('print(reduce(add,range(101)))得到的值是多少')
print(reduce(add,range(101)))
#reduce 将[1,4,7,9,5,3,5]合并成10进制的书
def fn(x,y):
    return x*10 + y
print(reduce(fn,[1,4,7,9,5,3,5]))
#str变成int的函数
def str2int(s):
    def fn(x,y):
        return x*10 + y
    def char2num(m):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[m]
    return reduce(fn,map(char2num,s))
print(str2int('19874567')*9)
#这里char2num的返回值实际上就是通过字典的语法，读出字典key对应的value，达到char转num目的
#再把转换成列表的num，转换成int
#练习利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
#def normalize(name):
#   namexiao =  name.lower()
#   namefenli = list(namexiao)#注意一定要这一步，直接用list(name)的话会，无论如何操作这个list都是指定的
#   namefenli[0] = namefenli[0].upper()#这里将第一个字符大写
#   def aplus(x,y):
#       return x+y#字符串相加即代表合并
#   return reduce(aplus,namefenli)
#def normalize(name):#第二种方式
#    return [name[m].capitalize() for m in range(3)]
#第三种方式
def normalize(name):
    for nalst in name:
        nalst = name.lower()
        nalst = nalst[0].upper() + nalst[1:]
    return nalst
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))#一定要这一步，map类似是一个生成器，所以必须用list把他显性化
print(L2)
#上述步骤简化版本
def normalize2(name):
    return name[0].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L3 = list(map(normalize2, L1))
print(L3)
#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
#def prod(L): 
#    def qiuji(x,y):
#        return x*y
#    return reduce(qiuji,L)#关键在于定义reduce中第一个函数的计算方式
#print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
#第一种方式
#def prod(L): 
#    sum = 1
#    for m in L: 
#        sum = sum * m 
#    return sum
#第二种方式1030
def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    def f1(x,y):
        return x*10 + y
    def f2(x,y):
        return x/10 + y
    def str2num(m):
        return {'.': 0,'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[m]
    def fenli(s):
        sz = [x for x in s if(x = '.') break]
    numlst = map(str2num,s)
    dotnum = dot(s)
    sz = 

