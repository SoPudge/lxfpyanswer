# -*- coding: utf-8 -*-
import time,threading
def loop():
    print('thread %s is runing...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
    print('thread is alive: %s' % threading.current_thread().is_alive())

print('thread %s is running...' % threading.main_thread().name)
t = threading.Thread(target = loop)
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
#这里仍然是通过threading.Thread来创建一个线程实例，并且通过start方法调用，通过join方法阻塞主线程
#每个进程在执行的时候，都会创建一个主线程，称之为MainThread，然后再创建子线程，默认命名为Thread-1
#值得注意的是，这里只创建了一个子线程，作用是循环打印数字，而不是创建了5个子线程

# 假定这是你的银行存款:
balance = 0
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
#开启两个线程的原因是两个毫无相干性的线程修改同一个值，有时候在线程中断的时候，会导致执行的内容不一致

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()#实例化一个锁定对象方便调用
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()#告知线程修改时需要锁定
        try:
            change_it(n)
        finally:
            lock.release()
#try finally保证try后面执行成功后，finally后面一定会执行
#值得注意的是，加锁后一定要解锁，否则后面的代码无法修改内容
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#python 中的GIL，多线程使用的一些问题
import threading,multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target = loop)
    t.start()
