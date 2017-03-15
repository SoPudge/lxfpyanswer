# -*- coding: utf-8 -*- 
#在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：
#
#    '00\d'可以匹配'007'，但无法匹配'00A'；
#
#    '\d\d\d'可以匹配'010'；
#
#    '\w\w\d'可以匹配'py3'；
#
#.可以匹配任意字符，所以：
#
#    'py.'可以匹配'pyc'、'pyo'、'py!'等等。
#
#要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：
#
#来看一个复杂的例子：\d{3}\s+\d{3,8}。
#
#我们来从左到右解读一下：
#
#    \d{3}表示匹配3个数字，例如'010'；
#
#    \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
#
#    \d{3,8}表示3-8个数字，例如'1234567'。
#
#综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。
#
#如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。
#
#但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。

#######进阶######

#要做更精确地匹配，可以用[]表示范围，比如：
#
#    [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
#
#    [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
#
#    [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
#
#    [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
#
#A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
#
#^表示行的开头，^\d表示必须以数字开头。
#
#$表示行的结束，\d$表示必须以数字结束。
#
#你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。

import re
print(re.match(r'^\d{3}-\d{8}$','027-87526532'))
#匹配电话号码成功

####切分字符串####
print(re.split(r'\s+','a b  c'))
#类似excel当中的分列，按空格来分列
print(re.split(r'[\s\,]+','a b , d ,e   f'))
#中括号和后面的加号表示合集运算

####分组####
m = re.match(r'^(\d{3})-(\d{3,8})$','027-83215327')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())
#print(m.group(3))
#正则当中用小括号称之为分组，定义了分组的正则表达式，可以通过group方法提取对应分组的内容
#例如上例当中group(0)永远代表原始字符串，从1开始代表第一个分组，以此类推
#而使用groups()方法则是把所有分组匹配的内容放在tuple当中

####贪婪匹配####
m = re.match(r'^(\d+)(0*)$','102300')
print(m.groups())
#这里匹配的结果并不如我们所想，匹配出来的tuple是('102300', '')
#原因在于正则是默认贪婪匹配，导致\d+这个分组把开头数字后面的所有内容都匹配了，+代表至少匹配一个

m = re.match(r'^(\d+?)(0*)$','102300')
print(m.groups())
#通过问号，告诉正则使用非贪婪模式，所以可以匹配出结尾为0的分组


####分组####
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-876542').groups())
print(re_telephone.match('010-4567').groups())
#通过re.compile方法编译正则表达式，方便日后使用

####练习####
#请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#
#someone@gmail.com
#bill.gates@microsoft.com
#
#版本二可以验证并提取出带名字的Email地址：
#
#<Tom Paris> tom@voyager.org

m = re.compile(r'^\w+.?\w+@\w+.\w+')
print(m.match('someone@gmail.com'))
print(m.match('someone.abc@gmail.com'))

n = re.compile(r'<(.*)>\s*(\w+.?\w+@\w+.\w+)')
print(n.match('<Tom Paris> tom@voyager.org').groups(1))