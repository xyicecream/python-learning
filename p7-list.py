#列表list: 能装东西的东西
#在Python中用【】表示一个列表，列表中的元素用，隔开
#a = ["张三丰","张无忌","周芷若",[1,2,3]]

#4.1特性
#1.也像字符串一样有索引和切片
#2.索引超过范围会报错
#3.可以用for循环来遍历
#4.用len 可以得到列表的长度
# lst = ["Anna","baby","cc","xixi"]
# print(lst[0])
# print(lst[1:3])
# print(lst[::-1])
# for item in lst:
#     print(item)
# print(len(lst))

#=========================
#4.2 列表的增删改查***
# lst = []
# #向列表中添加内容
# # append()追加 ***
# lst.append("xy")
# lst.append("cc")

# # insert() 插入
# lst.insert(0,"赵敏")

# #extend()
# lst.extend(["haha","张无忌"]) #合并两个列表
# print(lst)

# #删除
# ret = lst.pop(3) #给出被删除的索引，返回被删除的元素
# print(lst)
# print(ret)
# lst.remove("cc") #删除某个元素 .remove() ***
# print(lst)

# #修改
# lst[4] = "mie" #直接用索引修改
# print(lst)

# #查询
# print(lst[1]) #直接用索引来查询

# #eg:
# # 吧所有姓张的人修改成姓王
# lst = ["赵敏","张绍刚","张无忌","武则天","嬴政","马超"]
# #for item in lst: # 这么写没办法获得每个元素的索引位置
# for i in range(len(lst)):
#     item = lst[i]
#     if item.startswith("张"):
#         new_name = "王"+item[1:]
#         print(new_name)
#         #把新名字放到列表中的原位置
#         lst[i] = new_name #修改完成
# print(lst)


#4.3列表的其他操作
#排序
# lst = [1,2,3,'aa'] #列表会按照存放的元素顺序保存
# print(lst)

# lst = [222,444,555,43,23,123,24324,111]
# lst.sort() #对列表进行升序排序
# lst.sort(reverse = True) #降序排序
# print(lst)

# #列表的嵌套
# lst = ['abc','111',['xixi','cc',[123,'scarpy']],'qwe','shjak']
# print(lst[2][2][1])
# lst[2][2][1] = lst[2][2][1].upper()
# print(lst)

# 列表的循环删除
lst = ["赵敏","张绍刚","张无忌","武则天","嬴政","马超"] #删除所有姓张的
temp = [] #建一个空表用来存储要删除的内容
for item in lst:
    if item.startswith('张'):
        temp.append(item) #把要删除的内容记录下来
        #lst.remove(item) # 有bug，但是不报错
for item in temp:
    lst.remove(item) # 去原列表中进行删除操作
print(lst)

#安全稳妥的循环删除方式：
#  将要删除的内容保存在一个新列表中，循环新列表，删除老列表

