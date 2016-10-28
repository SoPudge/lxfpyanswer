#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test module'
__author__ = 'Jonchil Zhang'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello,world!')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')
if __name__ == '__main__':
#详见evernote解释
    test()
    print('尼玛')
print(test.__name__)
def yhsj(h):
    L = [1]
    for i in range(1,h):
        yield L
        L.append(0)
        L = [L[i] + L[i-1] for i in range(1,h)]
