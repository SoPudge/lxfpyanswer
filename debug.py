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
#assert是断言的意思是断言后面跟的内容如果满足，则什么都不做，否则执行显示断言后半段内容
#此处n=0的话，则断言不成立，那么执行n is zero
import logging
logging.basicConfig(level = logging.INFO)
s = '0'
n = int(s)
logging.info('n = % d' % n)
print(10 / n)
#logging输出错误的信息
s = '0'
n = int(s)
print(10/n)
#pdb可以单步执行代码，按n单步执行代码，按p可以显示变量

