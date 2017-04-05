# -*- coding: utf-8 -*- 
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM user WHERE score BETWEEN ? and ? ORDER BY score',(low,high))
        values = cursor.fetchall()
        result = list(map(lambda x:x[0],values))
    finally:
        cursor.close()
        conn.close()
        return result

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print('Pass')
#本例需要注意的是，cursor.fetchall返回的是一个list，包含结果，结果在list当中是tuple的形式
#而利用map和lambda的原因是，map对values中的每个元素作用，通过lambda解析tuple，获取元素的字符串
#再利用list方法，把其变成列表返回
#通过finally执行关闭数据库对象的操作
