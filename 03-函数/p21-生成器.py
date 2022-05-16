'''
1.生成器的本质是迭代器

  创建生成器的两种方案：
    1.生成器函数
    2.生成器表达式

  生成器函数
     生成器函数有一个关键字yield
     生成器函数执行的时候，并不会执行函数，得到的是生成器

     yield：只要函数中出现了yield，他就是一个生成器函数
         作用：
           1.可以返回值
           2.可以分段执行函数中的内容，通过__next__()可以执行到下一个yield位置

    优势：
      用好了，特别节省内存


2.推导式：
     简化代码
     语法：
        1.列表推导式: [数据 for循环 if判断]
        2.集合推导式: {数据 for循环 if判断}
        3.字典推导式: [k:v  for循环 if判断}
        (数据 for循环 if判断) 不是元组推导式，这是生成器推导式
        
3.生成器表达式 -> 一次性的
  语法：(数据 for循环 if判断)


'''

# def func():
#     print(123456)
#     yield 999 # yield 也有返回的意思
#     print(777)
#     yield 888

# ret = func()
# #print(ret)  # <generator object func at 0x104d4dd90>
# #print(ret.__next__()) # yield只有执行到next的时候才会返回函数
# #ret.__next__() 

# print(ret.__next__())
# print(ret.__next__())

# # 去定制1000件衣服
# def order():
#     lst = []
#     for i in range(1000):
#         lst.append(f"衣服{i}")
#     return lst

# s = order()
# print(s)

# def order():
#     lst = []

#     for i in range(1000):
#         lst.append(f"衣服{i}")
#         if len(lst) == 50:
#             yield lst 
#             #下一次拿数据
#             lst = []
# g = order()
# print(next(g))

# lst = [i for i in range(10)] # 和直接写for循环存储列表一样
# print(lst)

# 1. 请创建一个列表【1,3,5,7,9】
# lst = [i for i in range(1,10,2)]
# lst = [i for i in range(10) if i % 2 ==1]
# print(lst)

#2. 生成50件衣服
# lst = [f"衣服{i}" for i in range(50)]

#3. 将列表中的英文字母都改成大写
# lst1 = ["abc","qwo","xyz","lmn"]
# lst2 = [item.upper() for item in lst1]
# print(lst2)

#4. 将下列的列表修改成字段，要求索引为key，数据作为value
# lst= ["赵敏","张无忌","周芷若","小昭"]
# dic = {i:lst[i] for i in range(len(lst))}
# print(dic)


gen = (i**2 for i in range(10)) #生成器
#print(next(gen))
for item in gen:
    print(item)
lst = list(gen) # list() 里面有for循环 一定要next()
print(lst)
