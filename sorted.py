# -*- coding: utf-8 -*-
#假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
L2 = sorted(L,key = lambda x:x[0].lower())
print(L2)
def by_score(t):
    return t[1]#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
L2=sorted(L,key=lambda x:x[1])
print(L2)
