import re
import urllib.request

res = urllib.request.urlopen("http://www.baidu.com/")
html = res.read()
print(html)

url = res.geturl()
print(url)