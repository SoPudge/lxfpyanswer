# -*- coding: utf-8 -*- 
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.baidu.com',80))
s.send(b'GET / HTTP/1.1\r\nHost: 10.166.49.28\r\nConnection: close\r\n\r\n')
#以上建立socket连接，并发送数据

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
#接收返回数据

s.close
#关闭连接

header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('index.html','wb') as f:
    f.write(html)
#接收数据并解析写入文件
