# -*- coding: utf-8 -*-
import functools#导入工具
def now():
    print ('2015-05-06')
f = now()
print('##########################')
def log(func):
    def wrapper(*args,**kw):
        print('call ',func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print ('2015-05-06')
now()
print(now.__name__)#经过装饰后的now名称已经变成了wrapper了，这就是装饰器
print('##########################')
#function.wraps的作用举例
def decoration(func):
    def wrapper(*args,**kw):
        print('this is decoration func')
        return func(*args,**kw)
    return wrapper
@decoration
def myfunc():
    print('this is my own func')
#这里来测试@过后的函数，实际上就是其他的函数了，是否还是本身,打印为wrapper函数
print(myfunc.__name__)
myfunc()#这里打印的就是装饰之后的内容
#这里不需要用h=myfunc()的原因是在于myfunc已经变成了wrapper函数，wrapper有自行返回内容，所以直接执行就有返回值
print('##########################')
#如果加上function.wraps的话，原来的函数还是原来的
from functools import wraps#导入工具
def decoration(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('this is decoration func')
        return func(*args,**kw)
    return wrapper
@decoration
def myfunc():
    print('this is my own func')
print(myfunc.__name__)
myfunc()
#这里打印出来的内容就是原来的函数本身
print('##########################')
#练习：请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def decoration2(func):
    def wrapper(*args,**kw):
        print('begin call')
        func(*args,**kw)
        print('end call')
        return func
    return wrapper
#这里先定义func，即被装饰后的内容，然后再返回即可
@decoration2
def dayin():
    print('this is call')
dayin()
#再思考一下能否写出一个@log的decorator，使它既支持：
#@log     
#def f():
#        pass
#又支持：
#@log('execute')
#def f():
#    pass
