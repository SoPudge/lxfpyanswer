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
    r = 10 / 2
    print('result',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')
#当某些代码执行有可能发生错误的时候，可以用try运行该类代码，此时一旦try当中遇到错误，则跳转到except后面代码执行
#然后在执行finally后面的代码，无论是否执行except，都会执行finally后面代码
try:
    print('try...')
    r = 10 / int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:print('no error')
finally:
    print('finally...')
print('END')
#可以使用多个except来执行错误发现，如上
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s)*2
def main():
    bar('0')
#    try:
#        print(bar('0'))
#    except Exception as e:
#        print('Error:',e)
#    finally:
#        print('finally...')
#main()
#对于多层调用的情况，只需要在调用层进行捕获操作，即可确认问题出现
#如果不用try的话，错误会一直向上抛，直到最终错误出现的代码，可以确认错误从哪里出现
#但是一旦出现错误的话，程序就会异常结束，这样没意义，应当让python打印出错误来
import logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('END')
#通过日志记录，可以让问题打印，但是不暂停执行程序，程序正常执行完毕之后才会退出
#抛出错误可以自定义错误的类，然后执行
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value:%s' % s)
    return 10 / n
foo('0')
#可以从ValueError中派生一个自定义类，然后从该类当中抛出错误
