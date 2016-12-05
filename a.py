# -*- coding: utf-8 -*-
class myclass(object):
    def chen(self,a,b):
        return a+b
obj = myclass()
print(obj.chen(8,9))
h = getattr(obj,'chen')
print(h)
