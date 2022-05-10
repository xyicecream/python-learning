'''
1.算数运算
+ - * / % //整除
2.比较运算
  > < >= <= ==(判断左右两端是否一致) !=
3.赋值运算
  = += -= *=
  a +=b
  a = a + b
4.逻辑运算
  1. and 左右两端同时成立，结果才能成立
  2. or 有一个成立，结果就成立
  3. not 非，非真既假，非假即假
  当 and 和 or 以及 not同时出现时，最好加上括号，避免出现歧义
  运算顺序：
  先算括号 > 算 not > and > or
5.成员运算
  in 判断xxx在xxx出现了
  not in
'''
# # %算余数
# #用来判断是否是35的倍数
# n = int(input("输入一个数字："))
# if n % 35 == 0:
#      print("是35的倍数")
# else:
#      print("不是35的倍数")

# a = 10
# b = 20
# #print(a==b)
# # c = a
# # a = b
# # b = c 
# # print(a,b) 
# #python中互换操作
# a,b = b,a
# print(a)
# print(b)

# 逻辑运算
print(True and False)
print(True or False or True)