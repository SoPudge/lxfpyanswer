# -*- coding: utf-8 -*- 
#本文档显示list关键字用法及他的几个方法
#关于list和tuple的用法#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###                                                                                                                            
# ##通用特点##
# list和tuple都是列表，区别是list是可变列表，tuple是固定列表，而固定列表
# 是在申明的时候就已经固定好了的，无法
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### 
list3 = ['1','2','3','8']
print ('list列表长度:len(list3) = ',len(list3))
print ('\n')
print ('list元素读取第一个:list3[0] = ',list3[0])
print ('\n')
list3.append('9') #先用append添加到末尾
print ('list元方法追加末尾append:list3.append(\'9\')= ',list3)
print ('\n')
list3.insert(1,'0')
print ('list元素方法insert插入元素到一个位置insert:list3.insert(1,\'0\')= ',list3)
print ('\n')
list3.pop(2)
print ('list元素方法删除指定位置元素，留空删除末尾:list3.pop(2)= ',list3)
print ('\n')
list3[0] = 5
print ('list替换指定元素:list3[0]=5 ',list3)

##tuple用法，只能一次创建，不能修改
T = (1,2,3,4,5,6,7)

##dict的用法
d = {'mic':1,'bob':2,'zzq':3}
print(d['mic'])

#修改mic的值
d['mic'] = 8
print(d['mic'])

#修改mic值之后，剩余的字典是什么，就是最新的数值823
print(d)
#验证dic内部元素
print('min' in d)
print('mic' in d)
print(d.get('mic',-9))

#删除一个key如何操作
d.pop('zzq')
print(d)

##set的用法:set存储一组key，但不带value，所以用list建立
s = set([1,2,2,5,6])
print(s)

s.add(3)
print(s)

s.remove(6)
print(s)
