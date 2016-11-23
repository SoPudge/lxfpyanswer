# -*- coding: utf-8 -*-
#利用特殊用途的函数对传统class进行改造称之为定制类
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'the name is %s' % self.name
print(Student('Jay'))
#第一种定制类，str，用这个得意义在于，直接调用类的时候，可以返回一个预定义的字符串，而不是类的地址
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)
it = Fib()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
#iter对象的意思就是在类中返回迭代器，因为类含有next对象，所以每次返回的self本身又具有next方法，所以可以不停地next
class Fib2(object):
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a
h = Fib2()
print(h.__getitem__(4))
print(h[4])
#通过getitem方法可以将类通过切片的方式引用，或者像list一样引用
class Student(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
s = Student()
print(s.name)
print(s.score)
class Chain(object):
    def __init__(self,value = ''):                    #这里是类对象的初始化，有一个默认参数传入，默认参数为空，同样也可以传入一个字符串
        self._path = value                            #执行的结果就是Chain类的_path属性等于传输的字符串，或等于空
    def __getattr__(self,value1):                      #Chain类的实例如果引用了一个未定义的属性，则调到这里执行，同时可以也可以传输一个字符串参数
        return Chain('%s/%s' % (self._path,value1))    #执行的结果是返回一个Chain(self._path/value)的类，括号当中是字符串，上一步执行的字符串
    def __str__(self):                                #定义打印类本身的结果
        return self._path                             #定义的结果是实例，传入一个字符串，即初始化__init__的结果
    __repr__ = __str__                                #定义输入类本身，显示的结果，和打印类显示的结果一致
print(Chain().status.user.timeline.list)
#执行顺序讲解：
print(Chain().status)
#首先执行Chain()，打印结果为空，因为初始化的类本身没有传入字符串，所以self._path为空
#同时由于打印了类本身，触发了__str__方法，返回self._path，即返回空值
#而Chain()的属性是status，显然会跳转到__getattr__执行，此时，执行的结果是返回Chain('空/status')，空是由于上一步的Chain类初始化未传入参数造成的空，即Chain('/status')
#Chain('/status')执行的结果就是，这个Chain是__getattr__当中的，而非第一步当中的，给Chain类初始化的实例，传入一个'/status'字符串，并执行实例本身
#执行过程就是self._path = '/status'，由于执行Chain类本身，触发__str__，返回'/status'
#所以执行结果是/status
print(Chain().status.user)
#由于Chain().status执行的结果相当于Chain('/status')，所以这一步实际上就是Chain('/status').user
#相当于Chain的一个属性user的执行，user显然应当由__getattr__来执行，所以相当于初始化Chain的时候传入了参数'/status'，并执行user属性
#即self._path = value，传入的value='/status'，由于存在user，这里进入到__getattr__流程
#user参数在getattr当中就是传入值，即value1，所以结果就是Chain('/self._path/value1')，即Chain('/status/user')
#下一步执行Chain('/status/user').timeline，过程同上
#简单来说就是chain类执行init初始化，属性执行getattr，然后再返回一个chain类，依次循环执行，直到结束
#返回一个值 Chain('/status/user')
#第二种定制类是__iter__函数完成的，
