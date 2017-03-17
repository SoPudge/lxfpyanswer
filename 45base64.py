# -*- coding: utf-8 -*- 
import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
#这是加密字符串，和解密字符串，前面b'代表Byte，即以byte形式识别字符串
#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
#转换的内容含有斜杠，不能再URL当中使用
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
#可以在URL当中加密内容，比如中文
print(base64.urlsafe_b64decode(b'abcd--__'))
print(base64.urlsafe_b64encode(b'zhongqi.zhang'))

def safe_base64_decode(s):
    i = len(s) % 4
    if i == 0:
        return base64.urlsafe_b64decode(s)
    else:
        return base64.urlsafe_b64decode(s+(4-i)*b'=')
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
