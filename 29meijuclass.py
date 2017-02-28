# -*- coding: utf-8 -*- 
from enum import Enum,unique
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
    print(name,member,member.value)
#通过enum定义的类，通常是不可更改的常量
@unique
class weekday(Enum):
    sun = 0
    mon = 1
    tue = 2
    wed = 3
    thu = 4
    fri = 5
    sat = 6
day1 = weekday.mon
print(day1)
print(weekday.tue)
print(weekday['wed'])
#以上方法可以访问枚举类中的内容
print(weekday.thu.value)
print(day1 == weekday.sat)
print(weekday(1))
weekday(7)
