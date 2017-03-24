# -*- coding: utf-8 -*- 
from urllib import request
proxy_support = request.ProxyHandler({'http':'10.166.1.37:8080'}) 
opener = request.build_opener(proxy_support)
request.install_opener(opener)
requrl = 'http://m.51job.com'
with request.urlopen(requrl) as f:
    data = f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
    #print('Data:',data.decode('utf-8'))
    print('##########')
#这里前三行是代理设置，无需变化


req = request.Request(requrl)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    #print('Data:', f.read().decode('utf-8'))
