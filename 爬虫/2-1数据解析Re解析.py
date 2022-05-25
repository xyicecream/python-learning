'''
正则表达式： Re解析
Re模块
'''
#Re模块
import re
# # findall 匹配字符串中所有的符合正则的内容
# lst=re.findall(r"\d+","我的电话是:10086,我的女朋友电话是:10010")
# print(lst)

# #finditer:匹配字符串中所有的内容，返回的是迭代器,从迭代器中拿到内容需要.group()
# it = re.finditer(r"\d+","我的电话是:10086,我的女朋友电话是:10010")
# for i in it:
#     print(i.group())

# #search 找到一个结果就返回，返回的结果是match对象，拿数据需要.group()
# s = re.search(r"\d+","我的电话是:10086,我的女朋友电话是:10010")
# print(s.group())

# # #match是从头开始匹配
# # m = re.match(r"\d+","我的电话是:10086,我的女朋友电话是:10010")
# # print(m.group())

# #预加载正则表达式
# obj = re.compile(r"\d+")
# ret = obj.finditer("我的电话是:10086,我的女朋友电话是:10010")
# for it in ret:
#     print(it.group())

# ret = obj.findall("haha,$10000")
# print(ret)

s = '''<div class='jay'><span id ='1'>郭麒麟</span></div>
<div class='jj'><span id ='2'>啊哈</span></div>
<div class='jolim'><span id ='3'>一二</span></div>
<div class='sylar'><span id ='4'>布布</span></div>
<div class='tory'><span id ='5'>嘿嘿</span></div>
'''
# (?P<分组名字>正则)可以单独从正则匹配的内容中提取到xxx内容
obj = re.compile(r"<div class='.*?'><span id ='\d+'>(?P<wahaha>.*?)</span></div>",re.S) #re.S:让.能匹配换行符
res = obj.finditer(s)
for it in res:
    print(it.group("wahaha"))