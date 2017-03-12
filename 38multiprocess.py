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
#def long_time_task(name):
#    print('run task %s (%s)' % (name,os.getpid()))
#    start = time.time()
#    time.sleep(1)
#    end = time.time()
#    print('task %s runs %0.2f seconds.' % (name,(end-start)))
#
#if __name__ == '__main__':
#    print('parent process %s' % os.getpid())
#    p = Pool(4)
#    for i in range(5):
#        p.apply_async(long_time_task,args=(i,))
#    print('waiting for all subprocess done...')
#    p.close()
#    p.join()
#    print('all subprocess done.')

#注意多进程之间的执行一定是并行的，虽然是并行的执行，但是由于long_time_task中的sleep函数存在，执行时间仍然是有区别的
#而且通过p.join方法，可知在子进程执行的时候，父进程是阻塞的，待子进程全部执行完毕，父进程才会执行完毕，所以all subprocess done是最后执行的
#由于在if当中定义了Pool(4)，所以进程池只能同时并行4个进程，由于time.sleep的存在，4个并行进程的start时间按循环的先后顺序来
#但是子进程的结束时间要看随机的sleep函数何时完毕，所以最终每个子进程执行完毕打印task runs的顺序并不一样，因为执行时间不同
#需要注意的是，由于进程池只有4个进程，而for循环当中有0-4一共5个循环过程，所以当执行完0123四个进程中最快结束的那个后（最快是由sleep方法随机决定的）
#才会执行第5个进程，即for循环当中的4号循环，同时按照执行完成的先后顺序打印执行结果
#p.apply_async是非阻塞版本的多进程执行，所以在执行子进程的时候，子进程是并行执行的，并不会等待某个子进程结束后再执行另一个，执行允许只和for执行顺序有关
#而p.close则是关闭进程池，必须，p.join代表主进程阻塞，等待子进程执行完毕之后，再执行join方法之后的主进程内容

import subprocess
#print('$ nslookup www.python.org')
#r = subprocess.call(['nslookup','www.python.org'])
#print(r)
#
#print('$ nslookup')
#p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
#print(output.decode('utf-8'))
#print('exit code: ',p.returncode)
#这两个子进程的例子，用于在更复杂的子进程当中，其中call方法是popen方法的简化版本，可以快速调用系统命令，传入参数是一个list
#popen方法更加基础，可以传入一个list为命令，通过stdin,stdout,stderr获取对应的输入和输出数据
#pipe则是linux当中标准的进程通讯方式，在subprocess.Popen当中，接收stdin管道输入的数据，输出stdout和stderr当中输出的数据，需要培训communicate
#communicate接收一个参数，通过管道输入给stdin，并且返回两个参数，通过管道接收自Popen方法，即输出和报错
#所以在Popen方法之后，通过stdout管道输出到communicate方法，再通过communicate方法返回到output值，打印即结果

#例题：通过多进程ping www.baidu.com一共100次，并返回结果，看单进程耗时，和多进程耗时
#单进程耗时

def baidu_ping():
    p = subprocess.call(['ping','www.baidu.com','-c','4'])
    print(p)
    print('subprocess pid is: ', os.getpid(),os.getppid())
if __name__ == '__main__':
    s = Process(target=baidu_ping)
    s.start()
    s.join()
    print('ping pid is',os.getpid())
