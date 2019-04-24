# -*- coding:utf-8 -*-

from urllib import request

req = request.Request("https://www.baidu.com")
req.add_header("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")

resp = request.urlopen(req)

print(resp.read().decode('utf-8'))        