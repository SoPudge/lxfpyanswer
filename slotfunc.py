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
m = Student2('Slash')
print(k.age)
print(hasattr(k,'age'))
print(hasattr(m,'age'))
#给类绑定属性的话，是所有实例共有的，但是给实例绑定属性，是实例独有的
#下面演示给实例绑定一个方法
def set_age(self,age):
    self.age = age
from types import MethodType
Student.set_age = MethodType(set_age,Student)
k = Student('kloy')
z = Student('zop')
k.set_age(25)
z.set_age(35)
#print(k.age)
print(k.age,z.age)
#这里set_age是一个方法，而age则是方法的属性，方法运用到实例，所以age也是实例的属性
#给一个实例绑定方法，对别的实例无效，所以可以给类绑定方法，对所有实例生效，如下
Student.set_age = set_age
l = Student('Amy')
l.set_age(18)
print(l.age)
#以上两个例子，通过两种方法给Student绑定属性，第一种通过methodtype给类绑定属性，会导致方法成为全局方法
#一旦使用这个方法，会对类派生的所有实例都生效
#而通过简单的studnet.set_age = set_age的话，则可以分别对实例使用
#如果想要限定给某个类只能绑定某种属性，则可以用slots方法
class Student3(object):
    __slots__ = ('name','age')
p = Student3()
p.name = 'Jon'
p.age = 69
print(p.age,p.name)
p.gender = 'male'
print(p.gender)
#限定外的内容会报错
