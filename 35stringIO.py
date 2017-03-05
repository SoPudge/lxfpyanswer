# -*- coding: utf-8 -*-
from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue())
f.write(' ')
f.write('world!')
print(f.getvalue())

f = StringIO('Hello!\nhi!\ngoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
print(f.getvalue())
