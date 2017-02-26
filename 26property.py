# -*- coding: utf-8 -*-
#在使用类当中的属性的时候，如果直接赋值并且可修改的话，那么就给了可趁之机
#可以直接在实例当中给实例的属性赋值，修改属性的值，这样不安全，例如
class Student(object):
    def __init__(self):
        pass
s = Student()
s.myscore = 89
s.myscore = 56
print(s.myscore)
#如何查看类有多少个属性
print(dir(s))
#在这种情况下，可以在类当中定义两种方式，一种是写入，一种是读取，读写分离，安全
class Student2(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('not int')
        if value < 0 or value > 100:
            raise ValueError('not between 0 - 100')
        self._score = value
m = Student2()
m.set_score(88)
m.set_score(59)
print(m.get_score())
print(dir(m))
#以上例子当中，get和set都是类的方法，方法调用需要如同函数一样，如果其中有self，则省略，有参数，则必须传输参数
#而上例子当中set方法当中的value参数，则是纯粹的参数，而score因为在self实例后面，所以是属性
#以上例子做到了读取写入分离，无法在外部修改，当然，猜到了写入方法除外
#通过使用property装饰器，可以让实例直接将方法当作属性来调用，从而达到了即利用属性调用的方便，又用到了方法调用的安全性
class Student3(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('not int')
        if value < 0 or value > 100:
            raise ValueError('not between 0 - 100')
        self._score = value
n = Student3()
n.score = 90
print(n.score)
#这里的关键是搞清楚def后面是定义的方法，而return后面的self._score则是属性
#方法可以和属性重名，方便调用，当然方法也可以设置成set_score，同样调用的时候不用是用n.set_score()这种函数形式
#可以直接使用n.set_score = 这种形式，把方法当成属性来使用，前提是是用property
#property这种方式当中，有.setter的话，是一个写入方法，只有property的话就是一个只读方法
#所以@property想当时property(score).getter，setter则是相当于property(score).setter
class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @property
    def resolution(self):
        return self._width * self._height
    @width.setter
    def width(self,w_value):
        self._width = w_value
    @height.setter
    def height(self,w_height):
        self._height = w_height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
#这里可以理解为@property为一个装饰器，当是用@property的时候，以def width为例
#实际上就是width = property(width)，此时新的width是propery的一个实例，继承了他的方法
#所以新写一个width方法的时候，如果要修改值的话，就使用width.setter
#assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
