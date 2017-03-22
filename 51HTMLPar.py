# -*- coding: utf-8 -*- 
from html.parser import HTMLParser
from html.entities import name2codepoint
class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('<%s>' % tag)
    def handle_endtag(self,tag):
        print('</%s>' % tag)
    def handle_startendtag(self,tag,attrs):
        print('<%s/>' % tag)
    def handle_data(self,data):
        print(data)
    def handle_comment(self,data):
        print('<!--',data,'-->')
    def handle_entityref(self,name):
        print('&%s:' % name)
    def handle_charref(self,name):
        print('&#%s;' % name)
parser = MyHTMLParser()
parser.feed('''<html>
        <head></head>
        <body>
        <!-- test html parser -->
            <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
            </body></html>''')

#找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
