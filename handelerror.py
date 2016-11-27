# -*- coding: utf-8 -*-
def foo():
    r = some_function()
    if r == (-1):
        return(-1)
    return r
def bar():
    r = foo()
    if r == (-1):
        print('Error')
    else:
        pass
#一旦出错，还要一级一级上报，除此之外，可以使用try..except..finall
try:
    print('try...')
    r = 10 / 0
    print('result',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')
