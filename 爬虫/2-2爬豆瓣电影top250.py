import requests
import re
import csv

def func(a):
    url = f"https://movie.douban.com/top250?start={a}&filter="
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    resp = requests.get(url,headers = headers)
    page_content = resp.text


    #解析数据
    obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)'
    r'</span>.*?<p class="">.*?<br>(?P<year>.*?)'
    r'&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
    r'<span>(?P<num>.*?)人评价</span>',re.S)

    #开始匹配
    result = obj.finditer(page_content)
    # f = open("top250.csv",mode = "w",encoding="utf-8")
    # csvwriter = csv.writer(f) #创建writer对象
    temp = []
    for it in result:
        # print(it.group("name"))
        # print(it.group("year").strip())
        # print(it.group("score"))
        # print(it.group("num"))
        dic = it.groupdict() # 正则匹配中的组名和数值存入字段
        dic['year'] = dic['year'].strip()
        temp.append(list(dic.values()))
        # csvwriter.writerow(dic.values()) # writerow 写内容 一次写一行
    # f.close()
    # resp.close()
    return temp
    #print("over")

arr = []
for i in range(10):
 res = func(i*25)
 arr.extend(res)


f = open("top250.csv",mode = "w",encoding="utf-8")
csvwriter = csv.writer(f) #创建writer对象
for item in arr:
    csvwriter.writerow(item) # writerow 写内容 一次写一行
f.close()
resp.close()



