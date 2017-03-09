# -*- coding: utf-8 -*-
import os
print('Process(%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('i am a child process (%s) and my parent is %s' % (os.getpid(),os.getppid()))
else:
    print('i (%s) just created a child process(%s)' % (os.getpid,pid))
#windows系统当中没有os.fork的调用，所以会报错
from multiprocessing import Process
import os

def run_proc(name):
    print('run child process %s (%s)...' % (name,os.getpid()))

if __name__ =='__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('child process will start.')
    p.start()
    p.join()
    print('child process end')
