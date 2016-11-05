# -*- coding: utf-8 -*-
import functools
#偏函数就是把一个函数的某一个参数固定住，并返回一个新的函数，使之更加通用，调用更加方便
#举例int函数，本质是转换某一个数字为10进制的整数
f = int('12345')
print(f)
#如果我们想要转换成二进制的整数呢，Int提供一个可选参数，int(x,base=10)
f = int('12345',base = 10 )
print(f)
#20进制转换
f = int('12345',20)
print(f)

#而偏函数简化这种操作
int2 = functools.partial(int,base = 2)
print(int2('10000'))

#当创建functools的时候，实际上是传入了万能参数给int2，*args和**kw
#所以上例当中实际上是给Int2传入了kw={'base',2}
