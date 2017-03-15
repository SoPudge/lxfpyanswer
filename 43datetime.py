# -*- coding: utf-8 -*- 
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))
#这里datetime是模块，含有一个datetime类
dt = datetime(2015,4,19,12,20)
print(dt)
#获取指定日期的时间

dt = datetime(2015,4,19,12,20)
print(dt.timestamp())
#通过timestamp方法可以转换时间datetime到标准的timestamp
t = 1429417200.0
print(t)
print(datetime.fromtimestamp(t))
#通过datetime的fromtimestamp可以反向转换时间戳到标准时间
#但是需要注意的是，标准转换是本地时间，而非UTC标准时间
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)
#这是str转换成标准时间，注意strptime的参数当中月份和天必须是小写，python规定

now = datetime.now()
print(now.strftime('%A,%B %d %H:%M'))
#这里同样将标准时间转换成字符串


