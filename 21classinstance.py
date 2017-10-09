# -*- coding: utf-8 -*-
class Student(object): 
    pass
bart = Student()
print(bart)
print(Student)
#这里显示类和实例的名字
#下面验证给类绑定属性
bart.name = 'vicent'
print(bart.name)
print(dir(bart))
print(dir(Student))
#可以看到，给实例绑定了属性之后，可以直接使用
#但是给实例绑定属性，不代表给类也绑定了属性，该属性只对实例有效
#下面验证在类中直接定义方法
class Student2(object):
    def __init__(self,name,score):
        self.name1 = name
        self.score1 = score
bart = Student2('Bart Simpson',89)
print(bart.name1)
print(dir(bart))
#这里需要注意的是，在定义类当中，属性，方法，和参数的区别
#在上述例子当中，init为类的方法，该方法需要传入2个参数name和score
#而方法当中，有两个属性，或者说类有两个属性，name1和score1
#这两个属性等于传入的对应参数的值，属性名可以和参数名一致，为了美观

#数据的封装
#封装的好处是可以把对应的方法放到类当中，当有实力从类当中派生出来的时候，直接可以
#继承或者使用方法，而不用关心实现细节
class Student3(object):
    def __init__(self,name,score,grade):
        self.__name = name
        self._score = score
        self._grade = grade
    def get_score(self):
        print(self._score)
    def get_name(self):
        print(self.__name)
    def get_grade(self):
        print(self._grade)
    def print_stuInfo(self):
        print (self.__name,self._score,self._grade)
bart = Student3('jon',89,'A')
#print(dir(Student3))
bart.print_stuInfo()
bart.get_score()
bart.get_name()
bart.get_grade()
print(bart._score)#单下划线开头的，可以外部直接调用
print(bart.__name)#双下划线开头的属性，不能直接被调用
#双单下划线开头的方法，调用与否也与属性一致
#init的意义在于初始化实例，可以知道该类接收几个参数，分别干什么用
#后面的get方法，用于实现需求，方法可以在实例中调用，同时有self的原因是
#接收参数本身，因为bart.get_score()这种调用方式，本身就是传入了一个参数，就是实例本身
