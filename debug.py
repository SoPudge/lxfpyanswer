# -*- coding: utf-8 -*-
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n
def main():
    foo('0')
main()
#可以用print来打印调试信息，确认程序的错误信息
def foo(s):
    n = int(s)
    assert n != 0,'n is zero!'
    return 10 / n
def main():
    foo('0')
main()
#assert是断言的意思是断言后面跟的内容应该是TRUE，否则断言下面的内容就会出错
