#1.拿到页面源代码
#2.使用bs4进行解析，拿到数据

import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.lvguo.net/baojia/蔬菜/1000/"
resp = requests.get(url)
resp.encoding = "utf-8"
#print(resp.text)

#解析数据
#1. 把页面源代码交给beautifulsoup进行处理，生产bs对象
page = BeautifulSoup(resp.text,"html.parser")#指定html解析器
#2.从bs对象中查找数据
#find(标签，属性 = 值)
#find_all(标签，属性 = 值)
#table = page.find("table",class_="bjtbl") #class是python中的关键字，所以属性class加个_
table = page.find("table",attrs={"class":"bjtbl"})#和上一行是一个意思，避免class
#print(table)
f = open("菜价.csv",mode="w")
csvwriter = csv.writer(f)
trs = table.find_all("tr")[2:]
for tr in trs: #每一行
    tds = tr.find_all("td")
    name = tds[2].text # .text表示拿到被标签标记的名字
    price = tds[3].text
    csvwriter.writerow([name,price])
    #print(price)
f.close()

