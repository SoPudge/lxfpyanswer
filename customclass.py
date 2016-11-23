# -*- coding: utf-8 -*-
#利用特殊用途的函数对传统class进行改造称之为定制类
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'self.name is'%self.name
print(Student('Jay'))
#第一种定制类，str，用这个得意义在于，直接调用类的时候
