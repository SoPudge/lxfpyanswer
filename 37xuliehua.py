# -*- coding: utf-8 -*-
#pickle用于进程或者网络间传输程序状态的数据
#简单来说就是把对象序列化成一串字符，然后传输，然后由这么一段字符再还原成原来的状态
import pickle
d = dict(name = 'bob',age = 20,score = 90)
p = pickle.dumps(d)
print(p)
#这里通过dumps来将dict对象进行序列化
print(pickle.loads(p))
#这里通过loads来进行还原

f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()
#再次注意，在进行open的时候，必须定义open的方式才能进行对应的read或者write操作
#如wb即代表写二进制数据，此时无法进行读取操作
#这里将文件进行序列化，同时上例中的字典d，写入文件

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)
#这里还原文件，但是文件内容不变，因为只是读取，而非修改

import json
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
s = Student('bob',20,90)
#print(json.dumps(s))
#错误的原因是因为json接受字典类型的变量来转换，而类的实力显然返回的不是字典
print(dir(s))
print(json.dumps(s.__dict__))
f = json.dumps(s.__dict__)
print(json.dumps(s,default = lambda obj:obj.__dict__))
#一般实例都会拥有一个__dict__的属性，可以把实例转换成dict模式，专门用于json的转换
print(f)
print(json.loads(f))
#这里直接通过loads将序列化后的f转换成一个dict，是单引号的
#但是dict仍然不是标准的类实例，需要有一个方法将dict转换成实例
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
#这里通过字典的key-vale转换，传入一个字典，同时d['name']获取字典得值，放在Student当中，成为一个实例
print(json.loads(f,object_hook = dict2student))
#loads有一个object_hook方法，来传入转换函数，转换f从字典到实例
