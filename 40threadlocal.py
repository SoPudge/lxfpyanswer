# -*- coding: utf-8 -*-
def process_student(name):
    std = Student(name)
    do_task_1(std)
    do_task_2(std)
def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)
def do_task_2(std):
    do_subtask_2(std)
    do_sbutask_2(std)
#线程如果使用全局变量，需要加锁以防修改出错
#所以线程中推荐使用自己的局部变量，可以用一个dict存储对应的变量
import threading
local_school = threading.local()
def process_student():
    std = local_school.student
    print('Hello %s (in %s)' % (std,threading.current_thread().name))
def process_thread(name):
    local_school.student = name#这里是给local_school绑定了student属性
    process_student()
t1 = threading.Thread(target = process_thread,args=('Alice',),name='Thread-A') 
t2 = threading.Thread(target = process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

print('####################')
#threading.local第二例
local = threading.local()#初始化一个local对象 
local.tname = 'main'#初始化一个全局变量，方便每个线程当中复制这个变量并进行修订

def func(): 
    local.tname = 'notmain'+threading.current_thread().name
    print (local.tname)
  
t1 = threading.Thread(target=func) 
t2 = threading.Thread(target=func)
t1.start()
t2.start()
t1.join() 
t2.join()
#这里注意local属性一般是在主进程当中初始化一个threading.local()变量
#初始化变量之后的实例，可以给他绑定属性，绑定的属性用于每个线程的修改
#所以在每个线程当中都可以独立修改，和使用互不影响
#那么如果主进程想要读取线程当中的本地变量内容怎么办？
