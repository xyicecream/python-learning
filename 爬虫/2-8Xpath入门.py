#xpath 是XML文档中搜索内容的一门语言
# html是xml一个子集
# xpath解析
import requests
from lxml import etree
# tree = etree.parse("b.html")
# result = tree.xpath('/html') / 根节点 拿文字用/text()
#/book/author//nick //表示atthor里面所有的nick的东西 //表示后面
#/book/author/*/nick * 通配符
#/html/body/ol/li/a[@href="dapao"/text()]
#循环中 相对查找 ./a/@href 拿到属性值
# xpath的顺序是从1开始，【】表示索引；【@xxx=xxx】属性的筛选
url = "https://shanghai.zbj.com/search/f/?kw=saas"
resp = requests.get(url)
#print(resp.text)
#解析
html = etree.HTML(resp.text)
#拿到每一个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
for div in divs:#每个服务商信息
    price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip("￥") #处理抓取的数据，从列表提取出来，删除￥
    title = "saas".join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()")) # 因为标题是两段文字拼接起来的，找到源代码是用saas关联的，所以这么做
    company_name = div.xpath("./div/div/a[1]/div[1]/p/text()")[1].strip() #company_name[1].strip() 公司名字里面有好多空格
    location = div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
    print(title)