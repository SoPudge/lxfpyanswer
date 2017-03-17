# -*- coding: utf-8 -*- 
#第一种namedtuple
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,Point))
print(isinstance(p,tuple))
#namedtuple类似一个类，可以从tuple当中派生出另一种数据类型，即具备tuple的不可改变特性，同样可以使用
#英文点号，即属性的方式来调用
#如果要用坐标和半径表示一个圆形，同样可以使用namedtuple来表示
Circle = namedtuple('Circle',['x','y','r'])
circle = Circle(2,3,4)

#第二种deque
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('z')
print(q)
#deque是另外一种数操作类型，并且支持双向插入和删除，默认从右边
#并且deque是线程安全的，可以多线程同时写入

#第三种defaultdict
from collections import defaultdict
dd = defaultdict(lambda:'no key')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
#defaultdict和dict行为一致，唯一区别在于调用dict的时候，如果没有key存在
#则会返回预先定义的动作

#第三种ordereddict
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
d2 = {'a':1,'b':2,'c':3}
print(d2)
print(d)
#d和d2是一个dict的两种不同申请方式，而且是完全无序的
od = OrderedDict([('a',1),('b',2),('c',3)])
od2 = OrderedDict(a=1,b=2,c=3)
print(od)
#新orderedict必须用od方式来进行，排序才正确
#另外注意，orderedict是通过key的插入顺序来确定顺序的，而不是key本身大小来排序

#第四种Counter
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
#counter是一个排序器，详细参见python文档
print(Counter('gallahad'))
print(Counter({'red': 4, 'blue': 2}))
print(Counter(cats=4, dogs=8))
