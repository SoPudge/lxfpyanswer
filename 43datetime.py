# -*- coding: utf-8 -*- 
from datetime import datetime
now = datetime.now()
print(now)
#获取当前日期
print(type(now))
#这里datetime是模块，含有一个datetime类
dt = datetime(2015,4,19,12,20)
print(dt)
#获取指定日期的时间

print('utc转换本地时间')
dt = datetime(2015,4,19,12,20)
print(dt.timestamp())
#通过timestamp方法可以转换时间datetime到标准的timestamp
#标准的timestamp是一个浮点数，从1970.1.1到今天计算秒数
t = 1433121030.0 
print(t)
print(datetime.fromtimestamp(t))
#通过datetime的fromtimestamp可以反向转换时间戳到标准时间
#但是需要注意的是，标准转换是本地时间，而非UTC标准时间
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)
#这是str转换成标准时间，注意strptime的参数当中月份和天必须是小写，python规定

now = datetime.now()
print(now.strftime('%A,%B %d %H:%M')) #这里同样将标准时间转换成字符串

print('########')
from datetime import datetime,timedelta
now = datetime.now()
print(now)
#datetime(2015,5,18,16,57,3,540977)
print(now + timedelta(hours = 10))
print(now + timedelta(hours = -10,minutes = 20))
#通过timedelta可以方便的加减时间，而不用进行换算

print('本地时间转换成UTC时间')
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours = 8))
now = datetime.now()
print(now) 
dt = now.replace(tzinfo = tz_utc_8) 
print(dt)
#本地时间转换成UTC时间

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
#这是拿到UTC时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print(bj_dt)
#将UTC时间转换成北京时间
ty_dt = bj_dt.astimezone(timezone(timedelta(hours = 9)))
print(ty_dt)
#将北京时间转换成东京时间，可见只要时区正确，可以随意转换

#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
import re
from datetime import datetime,timezone,timedelta
def to_timestamp(dt_str,tz_str):
    dt_float = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz_num = int(re.match(r'^UTC(\+|\-)(\d{1,2}):00$','UTC+8:00').group(2))
    conv_time = dt_float.astimezone(timezone(timedelta(hours = tz_num)))
    return conv_time.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
#assert t1 == 1433121030.0, t1
print(t1)
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
#assert t2 == 1433121030.0, t2
#
#print('Pass')
