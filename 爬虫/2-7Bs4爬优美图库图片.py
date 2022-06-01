# 1.拿到主页面的源代码，然后提取子页面的链接地址href
# 2.通过href拿到子页面的内容，找到图片的下载地址 img -> src
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
domain = "https://www.umei.cc"
resp = requests.get(url)
resp.encoding = "utf-8" #处理乱码
#print(resp.text)
main_page = BeautifulSoup(resp.text,"html.parser")
alist = main_page.find("ul",attrs={"class":"pic-list after"}).find_all("a") # 主要是定位两次
#print(alist)
hlist = []
for a in alist:
    h = domain+a.get("href")
    # hlist.append(h) # 直接通过get可以拿到属性
     #拿到子页面的源代码
    child_page_resp = requests.get(h)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text
    #从子页面拿图片的下载路径
    child_page = BeautifulSoup(child_page_text,"html.parser")
    s = child_page.find("section",attrs={"class":"img-content"})
    img = s.find("img")
    src = img.get("src") #取到img中的图片下载地址
    # print(img.get("src"))
    # break #测试
    #下载图片
    img_resp = requests.get(src)
    #img_resp.content #这里拿到的是字节
    img_name = src.split("/")[-1] #拿到url中的最后一个/以后的内容
    with open(img_name,mode="wb") as f:
        f.write(img_resp.content) # 图片内容写入文件
        break
#     print("over",img_name)
#     time.sleep(1)
# print("all over")
