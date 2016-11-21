# -*- coding: utf-8 -*-
#验证获取对象的基本信息
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

#通过type判断参数的类型真假
print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

#除了判断基础数据类型，还能判断函数是什么性质的函数，内置的，通用的，还是虚拟函数等等
import types
def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

#除了使用type来判断，但是对于类的继承关系的判断，可以通过instance这种实例方式判断
print(isinstance([1,2,3],tuple))
#使用dir来获取一个对象的所有方法
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))
dog2 = MyDog()
print(len(dog2))
print(dog2.__len__())
#定义了len之后可以用以上的方式来进行len的长度查询
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))
#这是hasattr来判断是否有这个属性
setattr(obj,'z',19)
print(hasattr(obj,'z'))
print(obj.z)
print(obj.x)
objnew = MyObject()
print(hasattr(objnew,'z'))
#通过setattr来设置一个新的属性，新的属性只对实例obj有效，对新实例无效
print(getattr(obj,'z'))
fn = getattr(obj,'z')
print(fn)
