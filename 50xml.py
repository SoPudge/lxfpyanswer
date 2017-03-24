# -*- coding: utf-8 -*- 
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
    def end_element(self,name):
        print('sax:end_element: %s' % name)
    def char_data(self,text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
        <li><a href="/ruby">Ruby</a></li>
        </ol>
        '''
handler = DefaultSaxHandler()#初始化一个saxhandler对象，用于解析xml文件
parser = ParserCreate()#初始化一个XML创建方法，用于解析XML文件，其中有三个方法，start,end cahr分别解析XML文件的开始符号，结束符号
#和中间字符串
#注意，解析是事件驱动的，按照顺序来解析

parser.StartElementHandler = handler.start_element 
parser.EndElementHandler = handler.end_element 
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
print(parser.Parse)

print('###################')
#请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取当天和第二天的天气：

#http://weather.yahooapis.com/forecastrss?u=c&w=2151330

#参数w是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。

#from xml.parsers.expat import ParserCreate
#class WeatherSaxHandler(object):
#    def __init__(self):
#        self.weatherResult = {}
#    def startElement(self,name,attrs):
#        if name == 'yweather:location':
#            self.weatherResult['city'] = attrs['city']
#            self.weatherResult['country'] = attrs['country']
#        elif name == 'yweather:condition':
#            self.weatherResult['currenDay'] = attrs['date'][5:7]
#        elif name == 'yweather:forecast' and attrs['date'][:2] == self.weatherResult['currenDay']:
#            self.weatherResult['today'] = {'text':attrs['text'],'low':int(attrs['low']),'high':int(attrs['high'])}
#        elif name == 'yweather:forecast' and int(attrs['date'][:2]) == int(self.weatherResult['currenDay'])+1:
#            self.weatherResult['tomorrow'] = {'text':attrs['text'],'low':int(attrs['low']),'high':int(attrs['high'])}
#        #print(self.weatherResult)
        #print(name,attrs)

####第二种代码####
from xml.parsers.expat import ParserCreate 
from datetime import datetime,date,timedelta
print(date.today().year)
class WeatherSaxHandler(object):
    def __init__(self):
        self.weatherResult = {}
        self.dateStatus = 0
    def startElement(self,name,attrs):
        if name == 'yweather:location':
            self.weatherResult['city'] = attrs['city']
            self.weatherResult['country'] = attrs['country']
            print(name,attrs)
        elif name == 'yweather:forecast':
            if self.dateStatus == 0:
                self.weatherResult['today'] = {'text':attrs['text'],'low':int(attrs['low']),'high':int(attrs['high'])}
                self.dateStatus = self.dateStatus + 1
            elif self.dateStatus == 1:
                self.weatherResult['tomorrow'] = {'text':attrs['text'],'low':int(attrs['low']),'high':int(attrs['high'])}
                self.dateStatus = self.dateStatus + 1
            elif self.dateStatus >= 2:
                for self.dateStatus in range(2,14):
                    self.weatherResult[self.dateStatus] = {'text':attrs['text'],'low':int(attrs['low']),'high':int(attrs['high'])}
                    self.dateStatus = self.dateStatus + 1
    def EndElement(self,name):
        pass
    def charData(self,data):
        pass


data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
            <title>Yahoo! Weather - Beijing, CN</title>
                    <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
                            <yweather:location city="Beijing" region="" country="China"/>
                                    <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
                                            <yweather:wind chill="28" direction="180" speed="14.48" />
                                                    <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
                                                            <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
                                                                    <item>
                                                                                <geo:lat>39.91</geo:lat>
                                                                                            <geo:long>116.39</geo:long>
                                                                                                        <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
                                                                                                                    <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
                                                                                                                                <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
                                                                                                                                            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
                                                                                                                                                        <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
                                                                                                                                                                    <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
                                                                                                                                                                                <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
                                                                                                                                                                                        </item>
                                                                                                                                                                                            </channel>
                                                                                                                                                                                            </rss>
                                                                                                                                                                                            '''
def parser_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.startElement
    parser.Parse(xml)
    return handler.weatherResult
#调用
weather = parser_weather(data)
assert weather['city'] == 'Beijing', weather['city']
assert weather['country'] == 'China', weather['country']
assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
assert weather['today']['low'] == 20, weather['today']['low']
assert weather['today']['high'] == 33, weather['today']['high']
assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
print('Weather:', str(weather))
#首先需要了解XML读取是一个回调函数，并且是事件驱动的方法
#意思就是我们需要定义读取方法，由系统调用，遇到某一个标签，则调用某一个方法
#需要注意的是，如果要读取15天的天气预报，不能使用循环的方式，因为当读取到第三天的内容的时候，他是在第三天循环
#而不会顺序到第四天去读取，因为读取方式是面向过程的，一行一行的读取
