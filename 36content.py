# -*- coding: utf-8 -*-
#操作系统函数
import os
from datetime import datetime
print(os.name)
#print(os.uname())
#print(os.environ)
print(os.environ.get('PATH'))
print(os.environ.get('x','default'))
print('##########################################')
#操作文件和目录
print(os.path.abspath('.'))
#print(os.path.join(os.path.abspath('.'),'testdir'))
#print(os.rmdir(os.path.join(os.path.abspath('.'),'testdir')))
#print(os.mkdir(os.path.join(os.path.abspath('.'),'testdir')))
#可以通过os.mkdr来建立一个目录，但是注意引用的路径用函数表述，这样可以避免不同操作系统下面系统路径的格式问题
#拆分路径同样要用os.path.split函数
print(os.path.split(os.path.join(os.path.abspath('.'),'writefile.txt')))
print(os.path.splitext(os.path.join(os.path.abspath('.'),'writefile.txt')))
print('##########################################')
print([x for x in os.listdir('.') if os.path.isfile(x)])
#通过生成器来列表当前目录下所有文件，通过if来验证是否是文件还是目录
print([x for x in os.listdir() if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
#这里os.path.splitext(x)[1]代表的是，该函数将文件名分割成一个list，包含两项，第一项是文件路径，第二项是后缀名
#利用os模块编写一个能实现dir -l输出的程序。 #编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。 
#[print(fname) for fname in os.listdir('.')] 
for finfo in os.listdir('.'): 
    fsize = os.path.getsize(finfo) 
    mtime = datetime.fromtimestamp(os.path.getmtime(finfo)) 
    print(mtime,fsize,finfo)
#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def getstr():
    find_str = input('your want to find str: ')
    for listdir in os.listdir():
        if find_str in listdir:
            print(os.path.abspath(listdir))
getstr()
