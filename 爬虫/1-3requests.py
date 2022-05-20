#安装requests

import requests
# query = input("请输入一个搜索名：")
# url = f"https://www.sogou.com/web?query={query}" #网页地址栏写的一定是get请求
# #请求头
# dic = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
# resp = requests.get(url,headers = dic) # 处理反爬
# print(resp)
# print(resp.text) #拿到页面源代码

url = "https://fanyi.baidu.com/sug"
s = input("请输入一个英文单词：")
dat = {"kw":s}
#发送POST请求,发送的数据必须放在字典中，通过data参数进行传递
resp = requests.post(url, data = dat)
print(resp.json()) #将服务器返回的内容直接处理成json() => dict
