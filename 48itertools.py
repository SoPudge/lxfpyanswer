# -*- coding: utf-8 -*- 
import itertools
natuals = itertools.count(1)
#for n in natuals:
#    print(n)
#count方法会不断地重复，创建一个无限迭代器
#count接收两个参数时候，第二个参数代表步进值

cs = itertools.cycle([1,2,3,4,5])
#for c in cs:
#    print(c)
#cycle方法不断地重复一个序列

ns = itertools.repeat([1,2,3],4)
for n in ns:
    print(n)
#repeat方法重复一个值，并且第二个参数约定重复次数，没有第二个参数则无限重复

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x : x < 10,natuals)
print(list(ns))
#takewhile确保迭代器重复需要的次数，第一个参数是预定义的条件，第二个参数是迭代器

for c in itertools.chain('ABC','XYZ'):
    print(c)
x = [c for c in itertools.chain('ABC','XYZ')]
print(x)
#chain保证形成一个更大的器

for key,group in itertools.groupby('AABBAA'):
    print(key,list(group))
#如果相邻的两个元素返回值相等，则放在一个组
