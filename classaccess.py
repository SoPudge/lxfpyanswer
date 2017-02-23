# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))
bart = Student('simpson',78)
bart.print_score()
#print(bart.__name)
#在该例当中，用双下划线开头的属性，是无法直接访问修改的，代码健壮
#经过尝试，如果变量不带双下划线，则可以被外部访问修改
#例子2:上例无法直接获取到名字，那么想要单独获取名字，需添加获取名字的方法
class Student2(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))
    def get_name(self):
        return print(self.__name)
bart = Student2('simposn',79)
bart.get_name()
#例子3：上例可以获取名字，但无法修改名字，加入一个修改方法
class Student3(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))
    def get_name(self):
        return print(self.__name)
    def set_name(self,name):
        self.__name = name
bart = Student3('jon',90) 
bart.get_name()
bart.set_name('vicent')
bart.get_name()
#该例当中修改名字的方法传入一个参数name，并且将参数name的值赋给self.__name，就是修改属性__name的值
#而set_name方法和init方法当中传入的参数虽然都叫name，但不是一个参数
#而self.__name属性是类共有的，所以和init当中的属性都是同一个
#简单来说，变量可以名称修改，但类的属性一旦确认，不修改
