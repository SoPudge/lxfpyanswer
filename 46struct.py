# -*- coding: utf-8 -*- 
import struct
print(struct.pack('>I',20140099))
#把数字打包成bytes类型
print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))
#把bytes解码成需要的内容，注意>后面，I代表4字节无符号整数，和2字节无符号整数
#请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
def bmpinfo(bmpname):
    with open (bmpname,'rb') as f:
        fb = struct.unpack('>ccIIIIIIHH',f.read(30))
        if fb[:2] == (b'B',b'M'):
            print('是否是位图：%s' % 'yes')
            print('图片大小是 %s * %s，图片颜色是 %s' % (fb[6],fb[7],fb[9]))
            print(fb)
        else:
            print('不是位图')
bmpinfo('1.bmp')
#这里需要注意的是f.read后面跟数值，代表读取多少位二进制
#记住f.read读取的数值也是一个tuple，所以可以用切片的方式切分
