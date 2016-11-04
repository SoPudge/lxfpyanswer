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
        result= func()
        print('日志添加成功')
        return result
    return inner
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
#这里首先看到outer函数，并且返回了一个inner函数，outer函数读入内存不执行
#然后向下遇到了@outer，那么就会立即执行outer(f1)，执行过程如下
#首先建立outer(f1)，此时就有func = f1，就是func指向f1执行结果所在的地址
#然后执行到inner，将f1 = inner赋值，此时的f1就已经是inner内的内容了
#然后return返回inner，由于返回函数名，所以此时不显示任何东西
#上面步骤完成了func指向老f1，新f1指向inner的过程，以后调用就是调用的新f1，达到了新老结合装饰的目的
#最后调用新f1的话，就会执行inner的内容
#详细执行过程讲解见链接：http://www.cnblogs.com/feixuelove1009/p/5541632.html
#
#return = func()带括号的原因就是func()会执行，而func不会执行，所以一定要带括号，要执行老函数达到装饰目的
#return一个result的原因是调用f1的返回值，达到装饰器更进一步灵活装饰的目的，这里f1没有返回值，所以不返回内容
#原因是最终outer返回的是inner函数名，不会执行inner的结果，所以即使省略返回result，也不会返回默认的NONE
#为什么要在outer中封装两层呢，因为只封装一层的话，inner就会立即执行，不会等到后面调用f1
##############第四个例子##############
def outer(func):
    def inner(*args,**kwargs):
        print("认证成功！")
        result = func(*args,**kwargs)
        print("日志添加成功")
        return result
    return inner

@outer
def f1(name,age):
    print("%s 正在连接业务部门1数据接口......"%name)
    
# 调用方法
f1("jack",18)
#我们有*args和**kwargs嘛！号称“万能参数”！简单修改一下上面的代码：
##############第四个例子##############
#一个函数被多个装饰器装饰，顺序如何，请了解
#记住，多个装饰器的执行顺序是上下执行
def outer1(func):
    def inner(*args,**kwargs):
        print("认证成功！")
        result = func(*args,**kwargs)
        print("日志添加成功")
        return result
    return inner

def outer2(func):
    def inner(*args,**kwargs):
        print("一条欢迎信息。。。")
        result = func(*args,**kwargs)
        print("一条欢送信息。。。")
        return result
    return inner

@outer1
@outer2
def f1(name,age):
    print("%s 正在连接业务部门1数据接口......"%name)

# 调用方法
f1("jack",18)

