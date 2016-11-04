# -*- coding: utf-8 -*-
##############第一个例子##############
def foo():
    print('foo函数被执行了')
#foo()
#如果这里直接运行的话，不会返回任意内容
#因为def定义的内容python不执行，只读取到内存
#除非后续有调用
def foo():
    print('我是第2个foo函数哈哈')
foo()
print(foo())
#这里显示第二个foo的打印内容，因为第二个覆盖了第一个
#这里如果用print打印的话，会多打印一个none，原因是def不定义return的话，默认返回none
##############第二个例子##############
def foo():
    print('我们干点什么')
    return 'OK'
foo()
#这里直接调用函数，会运行打印的内容，但是不反回OK，因为你没有要求返回
#因为foo()只是函数本身内容的执行，并不涉及赋值，不用返回结果给谁，所以自然没有返回
h = foo()
print(h)
#这里因为运行了一个赋值操作，所以自然要把return的内容返回复制给h，同时打印h
##############第三个例子##############
def outer(func):
    def inner():
        print('我是内层函数')
    return inner

def foo():
    print('我是原始函数')

outer(foo)
print(outer(foo))
#这里一定要注意，return inner是不执行的，因为他返回的是函数名称
#这里执行的是foo函数名，函数名就是一个地址指针，并无return的值，所以不显示任何内容
#和上面一样，打印结果，返回的是一个地址
outer(foo())
print(outer(foo()))
#这里由于调用的是foo()，即代表调用的是函数的返回
#这里为什么不反回内存函数的文字，是因为outer中return返回的是inner的名字，而不是inner()的结果
##############第三个例子##############
#需求是加一个登陆验证模式
def f1():
    print('业务部门1数据接口……')
def f2():
    print('业务部门2数据接口……')
def f3():
    print('业务部门数据3接口……')
def f100():
    print('业务部门100数据接口……')

f1()
f2()
f3()
f100()

#通过装饰来添加
def outer(func):
    def inner():
        print('认证成功')
        result = func()
        print('日志添加成功')
        return result
    return inner()
@outer
def f1():
    print('业务部门1数据接口……')
@outer
def f2():
    print('业务部门2数据接口……')
@outer
def f3():
    print('业务部门数据3接口……')
@outer
def f100():
    print('业务部门100数据接口……')

f1()
f2()
f3()
f100()
#装饰器的作用相当于outer(f1())，用@语法糖来表示而已
#需要注意的是，在outer函数当中需要return一个result，把f1()的结果呈现出来，可以省略返回result
#原因是最终outer返回的是inner函数名，不会执行inner的结果，所以即使省略返回result，也不会返回默认的NONE
