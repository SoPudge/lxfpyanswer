#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#设计一个计算学生成绩的类，并且用实例表现出来
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
#这里直接定义print方法的意义在于，调用这个类的实例的时候，可以直接输出内容
#否则的话要print一次内容
std1 = Student('John',86)
std2 = Student('Vicent',46)
std1.print_score()
std1.print_score()
print(std1)
#这里会打印出一个内存地址，表明std是函数类的一个对象，就是实例
print(Student)
#这里会直接告诉你这是类的内存地址
