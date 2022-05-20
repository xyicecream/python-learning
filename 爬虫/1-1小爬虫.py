'''
爬虫: 通过编写程序来获取到互联上的资源
需求：用程序模拟浏览器，输入一个网址，从该网址中获取资源或者内容
python搞定以上需求：
'''
#首先导入一个包
from urllib.request import urlopen
url = "http://www.baidu.com"
resp = urlopen(url)
#print(resp.read().decode("utf-8"))
# 将爬出的信息保存到一个文件中
with open("mybaidu.html",mode = "w") as f:
    f.write(resp.read().decode("utf-8")) #拿到的是网页源代码
print("over")