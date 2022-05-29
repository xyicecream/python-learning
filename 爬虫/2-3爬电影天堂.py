#找到2022必看电影
import requests
import re
import csv

domain = "https://dytt89.com/"
resp = requests.get(domain)
resp.encoding = "gb2312" # 原网页是gb2312
#print(resp.text)
#拿到ul中的li
obj1 = re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S) # 匹配页面中的必看电影
obj2 = re.compile(r"<a href='(?P<herf>.*?)' .*?</a>",re.S)
obj3 = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?'
r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)
result = obj1.finditer(resp.text)
child_herf_list = []
for it in result:
    ul = it.group("ul")
    #提取子页面的链接
    result2 = obj2.finditer(ul)
    for it2 in result2:
        child_herf = domain + it2.group("herf").strip("/")
        child_herf_list.append(child_herf) #将子页面链接存到列表中
#print(child_herf_list)
#提取子页面内容
temp = []
for h in child_herf_list:
    child_resp = requests.get(h)
    child_resp.encoding = "gb2312"
    #print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    # print(result3.group("movie"))
    # print(result3.group("download"))
    #break #测试用
    dic = result3.groupdict()
    temp.append(list(dic.values()))
f = open("2022必看热片download.csv",mode="w",encoding="utf-8")
csvwriter = csv.writer(f)
for item in temp:
    csvwriter.writerow(item)
f.close



