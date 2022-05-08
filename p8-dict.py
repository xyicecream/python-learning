# 字典是以键值对的形式进行存储数据的
#字典的表示方式：{key:value,key2:value2,key3:value3}
# dic = {"jay":"周杰伦","金毛":"谢逊"}
# val = dic["jay"] #用key找值
# print(val)

#字典的key必须是可哈希的数据类型  （不可变的数据类型）
#字典的value可以是任何数据类型

# 4.2 字典的增删改查
# dic = dict()
# dic["jay"] = "周杰伦"
# dic[1] = 123
# print(dic)
# dic["jay"] = "昆凌" #字典中已经有了jay，就直接执行修改操作
# dic.setdefault("tom","cat") #设置默认值，如果之前有tom，setdefault就不起作用了
# print(dic)

# #删除
# dic.pop("jay") #根据key删除
# print(dic)

# #查询
# #print(dic["jay"]) #如果key不存在，程序会报错，当确定所有的key没问题
# #print(dic.get('jay111')) #如果key不存在，程序返回none。

# # None
# a = None #空类型什么都不能做
# print(type(a))

# 4.3字典的循环嵌套
dic = {"a":1,"b":2,"c":3,"d":4}
# # 1. 用for循环，直接拿到key
# for key in dic:
#     print(key,dic[key])
# # 2. 把所有的key都保存在列表中
# print(list(dic.keys())) #取出所有的keys
# # 3. 把所有的value放在一个列表中
# print(list(dic.values()))
# 4.直接拿到字典里的key和value
#print(list(dic.items()))

# for item in dic.items():
#     key = item[0]
#     value = item[1]
#     print(key,value)

# for item in dic.items():
#     #print(item) #确定item中只有两个元素
#     key,value = item
#     print(key,value)

# for key,value in dic.items(): #重要：可以直接拿到字典中所有的key和walue
#     print(key,value)


#a,b = (1,2)#元祖或者列表都可以执行该操作，该操作叫结构（解包）

# #字典的嵌套
# cc = {"name":"cc","age":28,"wife":{"name":"xx","age":28,"assitant":{"name":"ice","age":"22"}}
# }
# # CC老婆助理的年龄
# age = cc["wife"]["assitant"]["age"]
# print(age)

# cc["wife"]["age"] = cc["wife"]["age"] -2
# print(cc)

# 字典的循环删除
dic = {"张三丰":"太极拳","张无忌":"乾坤大挪移","赵敏":"蒙古郡主","周芷若":"九阴白骨爪"}
temp = [] #先定义一个新列表存放即将删除的内容
for key in dic:
    if key.startswith("张"):
        temp.append(key)
        #dic.pop(key) #错误不能直接删除 dictionary changed size during iteration
for t in temp:
    dic.pop(t)
print(dic)
