# -*- coding: utf-8 -*- 
class Query(object):
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print('Begin')
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    def query(self):
        print('Query info about %s..' % self.name) 

with Query('Bob') as q:
    q.query()
#open方法需要关闭，用with open方法可以简单方便的让python自动管理上下文，进入-执行代码-退出
#其本质是类中含有__enter__和__exit__方法，enter方法在进入前执行，exit方法再结束后执行
#__exit__方法接受三个参数，一个是exc_type执行结果

from contextlib import contextmanager
class Query (object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s..' % self.name) 
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
with create_query('amy') as q:
    q.query()
#通过contextmanager可以代替手工在类当中内置enter和exit方法，远离就是@contextmanager实际上一个是装饰器
#装饰器必须装饰一个生成器对象，必须是可迭代的对象，所以才有yield

@contextmanager
def tag(name):
    print ("<%s>" % name)
    yield
    print("<%s>" % name)
with tag('h1'):
    print('hello')
    print('world')
#执行过程首先是with语句执行tag当中的print语句，然后遇到yield，将结果返回，返回执行with当中的print语句
#当yield之后，下次循环继续执行yield后面的内容开始，即tag当中的第二个print
