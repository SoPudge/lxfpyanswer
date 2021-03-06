#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'
__author__ = 'Jonchil Zhang'
import sys
print(__name__)
print(__author__)
def test():
    args = sys.argv
#sys.argv是系统函数，代表给文件传入了几个参数，专门用于验证参数，他的默认参数是文件名称
#所以如果args==1的话，那么就代表没有传输参数
    if len(args) == 1:
        print('Hello,world!')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')
if __name__ == '__main__':
#详见evernote解释
    test()
#这个脚本被执行的时候，name 值就是 main ，才会执行 main()函数。如果这个脚本是被 import 的话，name的值不一样。main()函数就不会被调用。这个句子用来写既能直接运行，又能给其他python程序import，提供库调用的脚本
