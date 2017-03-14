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
def process_student()；
std = local_school.student
print('Hello %s (in %s)' % (std,threading.current_thread().name))
def process_thread(name):
    local_school.student = name
    process_student()
t1 = threading.Thread(target = process_thread,)
