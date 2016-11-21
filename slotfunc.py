# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self,name):
        self.name = name
s = Student('Bob')
print(s.name)
print(Student('Bob').name)
#可以直接给实例绑定属性,这里绑定的属性是给实例的，因为通过init初始化一个实例
#所以直接引用student.name是无效的
class Student2(object):
    name = 'Student'
    def __init__(self,name):
        self.name = name
print(Student2.name)
#这里可以通过直接给类一个name的属性，可以直接引用student2.name即可
k = Student2('Jay')
k.age = 18
print(k.age)

