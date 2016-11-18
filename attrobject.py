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

