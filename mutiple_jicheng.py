# -*- coding: utf-8 -*-
class Mammal(object):
    def mamprint(self):
        print('这是哺乳动物类')
class meat(object):
    def meatprint(self):
        print('这是肉食动物类')
class tiger(Mammal,meat):
    def tigerprint(self):
        print('这是老虎')
s = tiger()
s.mamprint()
print(isinstance(s,tiger))
#多重继承模式，可以让一个类继承多个类的方法
#如果多个父类包含相同的方法，只继承第一个方法
