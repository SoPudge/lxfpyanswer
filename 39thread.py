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

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target = loop)
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
#这里仍然是通过threading.Thread来创建一个线程实例，并且通过start方法调用，通过join方法阻塞主线程
#每个进程在执行的时候，都会创建一个主线程，称之为MainThread，然后再创建子线程，默认命名为Thread-1
#值得注意的是，这里只创建了一个子线程，作用是循环打印数字，而不是创建了5个子线程
