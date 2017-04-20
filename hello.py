# -*- coding: utf-8 -*- 
def application(environ,start_resopnse):
    start_resopnse('200 OK',[('Content-Type','text/html')])
    return [b'<h1>Hello,web!</h1>']
