# -*- coding: utf-8 -*- 
import socket 
import time
#####客户端#####
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarah']:
    time.sleep(1)
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
#连接对应的端口，同时第一次接收welcome信息
#然后通过循环，发送信息，接受返回信息并关闭连接
