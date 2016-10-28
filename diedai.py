# -*- cOding: UTF-8 -*- 
print('迭代一个list，遍历它，d = {\'a\': 1, \'b\': 2, \'c\': 3}')
d = {'a': 1, 'b': 2, 'c': 3}
for xxx in d:
    print(xxx)
    pass
print('默认情况下，迭代的是key，如果要迭代dict中的value，可以用x.values()')
for yyy in d.values():
    print(yyy)
    pass
print('默认情况下，如果要迭代key和value，如果要迭代dict中的value，可以用x.items()')
for xxx,yyy in d.items():
    print(xxx,yyy)
    pass
print('字符也可以迭代，abc')
for xxx in 'abc':
    print(xxx)
    pass
print('enumerate函数可以把一个list变成索引-元素对的形式')
L=['A','B','C','D','E']
print(L)
for m,n in enumerate(L,1):
    print(m,n)
    pass
