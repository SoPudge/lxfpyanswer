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
#初始化一个3开始的无限奇数list，这里面必然包含全部素数，是一个生成器
def odditer():
    n = 1
    while True:
        n = n + 2
        yield n
#判断是否是素数，原理就是所有素数都是在奇数中产生的，只需要测试前一步的奇数是否有约数
def ifsushu(n):
    return lambda x : x % n > 0
#结合生成素数的生成器函数，原理是先返回2，然后再while循环中不断循环返回新的list，并且通过filter测试这个list，测试完就返回测试成功的素数
def primes():
    yield 2
    it = odditer()
    while True:
        n = next(it)
        yield n
        it = filter(ifsushu(n),it)#这里用到参数n是因为素数都是奇数，所以只用测试odditer中的所有奇数，用ifsushu来测试是否被整除，测试函数是>0的，代表不能整除，即奇数
        #yield n
#上面内容的精华在while循环，其中fileter用it奇数列，来筛选其中每个数，是否可以整除大于1
#例如3 5 7 9 11 13 15 17 19，fliter用3来筛选这个数列，就去掉了可以被3整数的所有数，这都不是素数
#然后留下的数值，再继续同样的筛选即可
#这里需要注意，fliter筛选后的数列，仍然是原数列，所以next会获取下一个值来筛选
#见filter廖雪峰的课程，自己发帖说明了缘由
# 打印1000以内的素数:
for n in primes():
    if n < 500:
        print(n)
    else:
        break
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
#下面的代码是通过对比中位数两边的数字是否相等来测试回数，分奇数和偶数
#def is_palindrome(n):
#    n_lst = list(str(n))
#    n_len = len(str(n))
#    if n_len % 2 == 0:
#        if n_lst[0:n_len/2-1] == n_lst[n_len/2:n_len]:
#            return True
#    else:
#        if n_lst[0:(n_len-1)/2-1] == n_lst[(n_len-1)/2+1:n_len]:
#            return True
#下面的代码是直接对比数字正向和反向是否相等
def is_palindrome(n):
    return str(n) == str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))
