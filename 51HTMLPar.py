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

#parser.feed(open('pyevent.htm','r').read())
#parser.close()

#找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
class PythonWebConf(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tagStatus = False
    def handle_starttag(self,name,attrs):
        for k,v in attrs:
            if v == 'event-title':
                self.tagStatus = True
                print(attrs[0][1],':')
            elif k == 'datetime':
                self.tagStatus =True
                print('event-time: ')
            elif v == 'event-location':
                self.tagStatus = True
                print('event-location: ')
            elif v == 'say-no-more':
                self.tagStatus = False
    def handle_endtag(self,tag):
        self.tagStatus = False
    def handle_data(self,data):
        if self.tagStatus == True:
            print(data)
parser = PythonWebConf()
parser.feed(open('pyevent.htm','r').read())
#这里首先需要理解HTML读取的过程是怎样的，他是以事件为驱动的读取方式，也就是说，遇到了<h3>的时候，
#就会调用handle_starttag，遇到了</h3>的时候就会调用handle_endtag，遇到了数据的时候，就会调用handle_data
#它并不是处理完了starttag再处理endtag，再处理data的，读到哪里，处理到哪里

#而本题的最终目的是读取data内容，所以可以通过在starttag的过程当中，设置一个信号，信号为True，则读取后面的data
#否则不读取后面的data

#注意在读取event-title，和event-location的时候，都非常容易，因为他们只有一行，设置信号为True后，handle_Data函数会自动读取内容
#但是对于时间这个，他是由三排组成的<time>...<span><span></time>，我们读取的是...的内容，所以设置遇到time，信号为真，后面需要读取
#但这样的问题是，同样也会读取time标签内，嵌套的span标签的data，所以要认为设置span标签处为False，无需读取

#本例设置了一个信号，所以无法存储的一个{会议标题:(时间，地点)}这样的字典当中，在实际操作过程的时候
#可以对标题，时间，地点分别设置信号，在handle_data当中定义，遇到某个信号，存储到怎样的字典当中，是存储成key(即会议标题)
#还是存储到value[0]或者value[1]这养的详细信息当中
