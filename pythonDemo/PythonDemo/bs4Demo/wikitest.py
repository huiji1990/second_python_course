
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 请求URL并用UTF-8编码
resp = urlopen("https://baike.baidu.com/item/%E6%9D%83%E5%8A%9B%E7%9A%84%E6%B8%B8%E6%88%8F/70073?fromtitle=%E5%86%B0%E4%B8%8E%E7%81%AB%E4%B9%8B%E6%AD%8C&fromid=5284886&fr=aladdin").read().decode("utf-8")

# 使用BeautifulSoup解析
soup = BeautifulSoup(resp, "html.parser")

# 输出所有词条及对应URL
listUrls = soup.findAll("a",  href=re.compile("^/item/"))
for url in listUrls:
    if not re.search("\.(jpg|JPG)$", url["href"]):
        print(url.get_text(), "<------>", "https://baike.baidu.com" + url["href"])

