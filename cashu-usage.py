# -*- coding: utf-8 -*-
#函数的位置参数
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s*x
    return s
name1 = int(input('输入power参数计算x的n次方'))
name2 = int(input('输入N参数'))
print(power(name1,name2))
#默认参数举例2
#默认参数可以让输入更简单，可选
def enroll(name,gender,age=6,city='beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
name3 = input('请输入您的姓名：')
name4 = input('请输入您的性别：')
enroll(name3,name4)
#默认参数的坑
def add_end(L=[]):
    L.append('end')
    return L
print('请调用函数:')
add_end()
add_end()
print(add_end())
#可变参数举例
def cacl(num):
    sum = 0
    for n in num:
        sum = sum + n*n
    return sum
#必须构建一个list传入cacl当中才行,因为for了一个循环，num必须是list
#解决办法是def cacl（*num），将num视为可变参数
inpunum = []
m = 0
nums = int(input('请输入想计算平方和的数值'))
while m < nums:
    inpunum.append(m+1)
    m = m + 1
print(cacl(inpunum))
def cacl2(*num):
    sum = 0
    for n in num:
        sum = sum + n*n
    return sum
print(cacl2(1,2,3,4,5))
#i
#print(cacl(1,2,3,4,5))
#关键字参数，组装一个dict到函数中
def guanjianzi(name,age,**kw):
    print('name:',name,'age:',age,kw)
guanjianzi('张仲骐',16,city= 'beijing',gender = 'male') 
print('组装一个dict放到函数里') 
extra = {'张仲骐':16,'city':'武汉'}
guanjianzi('长追诉期',18,**extra)
#命名关键字参数的使用，命名关键字参数需要用一个星号隔开
#作用是限制传入参数的名称
def person(name,age,*,city,job):
    print(name,age,city,job)
#调用的时候，必须指明city=xxx,job=xxx才行，如下
print(person(1,2,city = 'wuhan',job = 'hr'))

#参数的组合
#在python中各种参数可以组合使用，但是顺序必须是：必选参数，默认参数，可变参数，关键字参数，命名关键字参数
def f1(a,b,c=0,*args,**kw):
    print(a,b,c,args,kw)
def f2(a,b,c=0,*,d,**kw):
    print(a,b,c,d,kw)
#记住，在命名关键字中，如果已经含有可变参数，则后面不需要再添加星号
print(f1(1,3,4,6,5,4,3,2,5,6,7,8,9,9,0,kw='test'))
print(f2(1,3,4,d='ddddddd',kw='test'))
#可以运行看看结果，其中f1和f2的区别就是，f1中abc是三个普通参数，后面跟上args一个可变参数，和一个kw的关键字参数
#所以f1当中，可以有无数个参数，函数只取得前三个为abc的值，命名关键字参数为最后一个，中间都是可变参数的值
#需要注意的是，在含有可变参数的组合当中，可变参数后面的参数一定要含有参数名的调用，而命名关键字参数本身无需
#f2的值当中，*除了分割命名关键字参数，其他无任何意义，同时*后面的参数调用，都必须包含参数名，即使普通参数也不例外
