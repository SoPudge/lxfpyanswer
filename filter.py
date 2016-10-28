# -*- coding: utf-8 -*-
#利用fliter保留一个list中的奇数
def odd(n):
    return n % 2 == 1
print(list(filter(odd,range(1,100))))
#删掉一个序列中的空字符串
def empty(s):
    return s and s.strip()
print(list(filter(empty,['A', '', 'B', None, 'C', '  '])))
#利用filter求素数
def odditer():
    n = 1
    while True:
        n = n + 1
        yield n
def ifsushu(n):
    return lambda x : x % n > 0
def primes():
    yield 2
    it = odditer()
    while True:
        n = next(it)
        yield n
        it = filter(ifsushu(n),it)
# 打印1000以内的素数:
for n in primes():
    if n < 50:
        print(n)
    else:
        break
#尝试一行代码求素数，实际上就是两次筛选，筛选奇数，再筛选素数
