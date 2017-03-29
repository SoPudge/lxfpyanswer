# -*- coding: utf-8 -*- 
import socket,threading,time
#####服务器####
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('waiting for connect...')
#服务器端首先绑定并监听端口，s.listen后面是指传入最大连接的数量

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        #time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
#定义tcplink，即每个线程的程序如何运行，如果有exit则退出程序

while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink,args = (sock,addr))
    t.start()
#开启多线程，同时处理tcp连接，其中target是指每个线程运行的程序，并传入两个参数
#两个参数来源s.accept()
