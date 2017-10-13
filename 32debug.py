# -*- coding: utf-8 -*-
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n
def main():
    foo('0')
#main()
#可以用print来打印调试信息，确认程序的错误信息
def foo(s):
    n = int(s)
    assert n != 0,'n is zero!'
    return 10 / n
def main():
    foo('0')
#main()
#assert是断言的意思是断言后面跟的内容如果满足，则什么都不做，否则抛出错误，显示后半段内容
#此处n=0的话，则断言不成立，那么执行n is zero
import logging
import pdb
logging.basicConfig(level = logging.DEBUG)
#pdb.set_trace()
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
#logging输出错误的信息
#插入pdb.set_trace()插入断点
s = '0'
n = int(s)
print(10/n)
#pdb可以单步执行代码，按n单步执行代码，按p可以显示变量
