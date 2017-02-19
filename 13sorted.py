# -*- coding: utf-8 -*-
#假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
L2 = sorted(L,key = by_name)#排序的核心就是key=后面是排序函数，可以用lambda也可以用自定义的def
#L2 = sorted(L,key = lambda x:x[0].lower())
print(L2)
def by_score(t):
    return t[1]#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
#L2=sorted(L,key=lambda x:x[1])
L2 = sorted(L,key = by_score)
print(L2)
#需要注意的是sorted接收的是list类型的参数，所以说给定的L实际上是个list，里面含有多个tuple
#所以定义的排序函数by_score的话，可以直接看成引用list当中的元素，即return t[1]，代表引用
#整个tuple，如果按字母排序，则小写，如果按数字排序，则返回数字，而sorted会自动排序
