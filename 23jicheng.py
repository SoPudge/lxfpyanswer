# -*- coding: utf-8 -*- 
class Animal(object): 
    def run(self):
        print('Animal is running...')
#定义一个animal类
class Dog(Animal):
    def run(self):
        print('dog is running...')
class Cat(Animal):
    def run(self):
        print('cat is running...')
        
#演示示例
husky = Animal()
husky.run()
dog = Dog()
dog.run()
#这里说明一种类可以继承父类的内容，达到复用的目的，但是子类含有父类相同的方法的时候
#执行顺序会是子类覆盖父类的相同方法

#判断一个类是否属于一个父亲类
print(isinstance(husky,Animal))

def run_twice(baba):
    baba.run()
    baba.run()
run_twice(Animal())
run_twice(Dog())
#这里说明新定义的函数，只要调用的对象是已知类或者其子类，就会自动具有类的方法
#无论这个类是已有或者新添加的，这个特性可以用于函数的后续调用
#显然在run_twice当中，传入一个baba的类，而执行的是传入类的run方法
#所以无论是父类还是子类，run_twice传入哪个，就执行对应的run方法
