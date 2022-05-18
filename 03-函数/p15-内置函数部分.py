'''
内置函数
1.基础数据类型相关
  1.和数字相关
    1.数据类型： bool,int,float,complex
    2.进制转换： bin,oct,hex
    3.数学运算： abs,divmod,round,pow,sum,min,max
  2.和数据结构相关：
    1.序列:
      1.列表和元祖: list, tuple
      2.相关内置函数: reversed, slice
      3.字符串: str,format,bytes,bytearry,memoryview,ord,chr,ascii,repr
    2.数据集合：
      1.字典: dict
      2.集合: set,frozenset
    3.相关内置函数: len, sorted,enumerate,all,any,zip,fiter,map
2.作用域相关
  locals： 函数会以字典形式返回当前位置的全部局部变量
  globals：函数会以字典类型返回全部全局变量
3.迭代器生成器相关
  range,next,iter


'''

# s = "123"
# i = int(s)
# b = bool(s)
# f = float(s)
#complex 复数：实部+虚部

# #bin，oct，hex
# a = 18 #十进制
# print(bin(a)) #二进制
# print(oct(a)) #8进制
# print(hex(a)) # 16进制

# b = 0b10010
# print(int(b)) #将二进制转化为十进制

# # sum,min,max,pow
# a  = 10
# b = 3
# print(pow(a,b)) # 次幂
# print(a ** b) # 次幂

# lst = [123,555,98,26,98,34,20]
# print(min(lst),sum(lst),max(lst))

# s = {1,2,3}
# lst = list(s) #内部一定有一个循环

# # format,ord,chr,
# # format
# a = 18
# print(format(a,"08b"))# b: 二进制 用0补齐8位

# zi = "中" # 在python的内存中使用的是unicode
# print(ord(zi)) # 给出文字在unicode中码位是20013
# print(chr(20013)) #给出编码位置，展示出文字
# for i in range(100):
#     print(chr(i)+" ",end="")

# all,any
# print(all([12,"呵呵","路"])) #当成and来看 true and true and true
# print(any([0,123,""])) #当成or来看

# #enumerate
# lst = ["一二","布布","小喵","小基"]
# for index,item in enumerate(lst):
#     print(index,item)
# for i in range(len(lst)):
#     print(i,lst[i])

# s = "xixi"
# print(hash(s)) # 一定是一个数字，想办法转化成内存地址，然后进行数据的存储 -> 字典（集合）哈希表

# # dir 当前这个数据能执行哪些操作

# ========================================


# zip 可以把多个可迭代内容合并
#把列表1,2,3中的索引0,1,2的所有元素列在一起
lst1 = ["赵本山","范伟","苏有朋"]
lst2 = [40,38,42]
lst3 = ["卖拐","耳朵大有福","情深深雨蒙蒙"]

# result = zip(lst1,lst2,lst3)
# # #print(result)
# # for item in result:
# #   print(item)

# lst = list(result)
# print(lst)

# # locals
# a = 188
# print(locals()) #此时locals被写在了全局作用域范围内，此时看到的就是全局作用与中的内容

# def func():
#   a = 336
#   print(locals()) #此时locals放在局部作用域范伟，看到的就是局部作用域的内容
# func()

# c = 12
# print(globals()) # globals看到的是全局作用域的内容

# def func():
#   d = 33
#   print(globals())
# func()


# sorted 排序
# lst = [23,49,12,444,1,5,99]
# s = sorted(lst,reverse = True)
# print(s)

# lst = ["卡卡","奥德赛","马里奥","塞尔达","刺客"]

# # def func(item): #item对应的就是列表中的每项数据
# #   return len(item)
# s = sorted(lst,key = lambda x: len(x)) # 一般lambda表达式配合sorted使用
# print(s)

# lst = [{"id":1,"name":"周润发","age":18,"salary":5600},
# {"id":2,"name":"周星驰","age":28,"salary":5111},
# {"id":3,"name":"周海媚","age":78,"salary":5612},
# {"id":4,"name":"周伯通","age":12,"salary":5321},
# {"id":5,"name":"周大兴","age":35,"salary":5987},
# {"id":6,"name":"周周","age":47,"salary":598},
# {"id":7,"name":"周扒皮","age":8,"salary":56},
# ]
# #根据每个人的年龄进行排序
# s = sorted(lst,key = lambda d : d['age'])
# print(s)

# #根据工资进行排序，从大到小
# s2 = sorted(lst,key = lambda d : d['salary'],reverse=True)
# print(s2)

# filter 筛选
lst = ["张无忌","张三丰","张翠山","灭绝师太","小狐仙"]
f = filter(lambda x: not x.startswith("张"),lst)
print(list(f))

#map: 映射
lst = [1,2,3,4,5,6,7,8,9]
r = map(lambda x: x*x,lst)
print(list(r))






