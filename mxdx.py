#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_object(self):
        print(self.name,self.score)

    def get_grade(self):
        if self.score >= 90:
            return "A"
        if self.score>= 60:
            return "B"
        else:
            return "C"
#测试类的用法
bart = student("myname",99)
bart.print_object()
print(bart.get_grade())
#修改变量测试
print(bart.score)
bart.score = 90
print(bart.score)
