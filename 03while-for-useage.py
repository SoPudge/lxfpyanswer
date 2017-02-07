# -*- coding: utf-8 -*-
#使用for in循环求和1-100
print('使用for-in循环求和1-100')
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
#使用while循环计算100以内偶数和
print('计算100以内偶数和使用while循环')
sum = 0
n = 98
while n > 0:
    sum = sum + n
    n= n-2
print(sum)
#利用循环一次对list中的每个名字打印出hello,xxx！
print ('利用foin-in打印L = [\'Bart\',\'Lisa\',\'Adam\']')
L = ['Bart','Lisa','Adam']
for x in L:
    print ('Hello ' + x)
#使用列表生成方式，记得使用中括号表示列表生成
print(['Hello ' + x for x in L])
print ('利用while打印L = [\'Bart\',\'Lisa\',\'Adam\']')
n = 0
while n < len(L):
    print(L[n])
    n = n + 1
