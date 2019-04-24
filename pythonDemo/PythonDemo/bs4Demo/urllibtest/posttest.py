# coding:utf-8

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("url")

postData = parse.urlencode([
    ("a", "b")
    ("c", "d")
    ])

req.add_header("User","")

resp = urlopen(req, postData=postData.encode("utf-8"))

print(resp.read().decode('utf-8'))    


