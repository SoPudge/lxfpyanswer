# -*- coding: utf-8 -*-
import functools#导入工具
def now():
    print ('2015-05-06')
f = now()
def log(func):
    def wrapper(*args,**kw):
        print('call ',func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print ('2015-05-06')
now()
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
print(myfunc.__name__,myfunc.__doc__)
print(myfunc())#这里打印的就是装饰之后的内容
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
print(myfunc.__name__,myfunc.__doc__)
print(myfunc())
#这里打印出来的内容就是原来的函数本身
