# -*- coding: utf-8 -*-
import os
#print('Process(%s) start...' % os.getpid())
#pid = os.fork()
#if pid == 0:
#    print('i am a child process (%s) and my parent is %s' % (os.getpid(),os.getppid()))
#else:
#    print('i (%s) just created a child process(%s)' % (os.getpid,pid))
#windows系统当中没有os.fork的调用，所以会报错
from multiprocessing import Process
import os

def run_proc(name):
    print('run child process %s (%s)...' % (name,os.getpid()))

#if __name__ =='__main__':
#    print('Parent process1 %s' % os.getpid())
#    p = Process(target=run_proc,args=('test',))
#    print('child process will start.')
#    p.start()
#    p.join()
#    print('child process end')
#注意，这里的父进程，就是文件执行本身的进程
#通过Process创建子进程实质上就是用Process建立一个实例，其中target参数代表子进程调用的对象，args代表给调用对象传入的参数
#对子进程实例进行p.start()操作，代表开始子进程，join方法代表阻塞当前进程，先调用子进程，执行完毕之后再执行后面的内容
#如果没有join方法，则会向下执行，在执行子进程调用的对象
#而if后面的print内容，则是if执行完毕之后会执行的内容
print('##############################')
#第二个Process实例，python文档当中的
#def info(title):
#    print(title)
#    print('module name:', __name__)
#    print('parent process:', os.getppid())
#    print('process id:', os.getpid())
#
#def f(name):
#    info('function f')
#    print('hello', name)
#
#if __name__ == '__main__':
#    info('main line')
#    p = Process(target=f, args=('bob',))
#    p.start()
#    p.join()
#这里在if后面就是按先后顺序执行，但将进程实例化成p之后，由于由join方法的存在，先执行子进程
from multiprocessing import Pool
import os,time,random

#for i in range(5):
#    print(i)
def long_time_task(name):
    print('run task %s (%s)' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random())
    end = time.time()
    print('task %s runs %0.2f seconds.' % (name,(end-start)))

if __name__ == '__main__':
    print('parent process %s' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('waiting for all subprocess done...')
    p.close()
    p.join()
    print('all subprocess done.')
