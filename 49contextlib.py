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
#with语句实际上是通过类的enter和exit方法实现的，所以只要一个类含有这两个方法，均可以
#通过with语句来进行读取

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

with create_query('Jac') as q:
    q.query()
