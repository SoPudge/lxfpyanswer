# -*- coding: utf-8 -*- 
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('',8000,application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()
#这里需要注意的是，作为一个服务器，只要是有访问服务器的动作，既是http请求，就会响应application函数当中的内容
#application 来自于hello.py当中的application方法
#environ则是用户提交的http请求信息
