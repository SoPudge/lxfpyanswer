# -*- coding: utf-8 -*- 
#from email.mime.text import MIMEText
#msg = MIMEText('hello,send by Python...','plain','utf-8')
#from_addr = input('From:')
#password = input('Password:')
#to_addr = input('To:')
#smtp_server = input('SMTP server：')
#
#import smtplib
#server = smtplib.SMTP(smtp_server,25)
#server.set_debuglevel(1)
#server.login(from_addr,password)
#server.sendmail(from_addr,[to_addr],msg.as_string())
#server.quit()
#可以发送成功，但是返回错误代码554，意思是被识别成垃圾邮件，用的网易邮箱发送到QQ

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP server:')

msg = MIMEText('hello,send by Python...','plain','utf-8')
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……','utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
