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
#这里将文件进行序列化，同时上例中的字典d，写入文件

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)
#这里还原文件，但是文件内容不变，因为只是读取，而非修改

import json
class Student(object):
