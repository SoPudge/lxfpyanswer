# -*- coding: utf-8 -*- 
import hashlib
md5 = hashlib.md5()
md5.update('jonchilzhang'.encode('utf-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('jonchil'.encode('utf-8'))
md5.update('zhang'.encode('utf-8'))
print(md5.hexdigest())
#可以分两次来进行hashmd5的操作，但是分两次进行的操作，必须保证写入同一个md5实例，才和一个md5出来的内容一致
#如果第七不重新申明一个实例的话，会导致3个md5同时计算

sha1 = hashlib.sha1()
sha1.update('jonchil'.encode('utf-8'))
sha1.update('zhang'.encode('utf-8'))
print(sha1.hexdigest())

#练习
def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()
db = {}
def register(username,password):
    db[username] = get_md5(password + username + 'thesalt')
def login(username,password):
    if db[username] == get_md5(password + username + 'thesalt'):
        return '登录成功'
    else:
        return '失败'
register('w','q')
print(login('w','r'))
print(login('w','q'))
