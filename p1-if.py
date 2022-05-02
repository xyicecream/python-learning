# #第一种if语法
# money = 500
# if money > 300:
#     print("出去嗨")
# print("回家")

# # 第二种if语法
# money = input("请输入有多少钱:")
# money = int(money)
# if money > 500:
#     print("hang out")
# else:
#     print("go back")

#第三种if语法 if嵌套语句
# money = int(input("how much money:"))
# if money >1000:
#     if money >5000:
#         print("buy a LV")
#     else:
#         print("have a nice dinner")
# else:
#     print("go back")

#第四种if语法 
money = int(input("how much money:"))
if money >5000:
     print("buy a LV")  
elif money >1000:
    print("eat")
else:
    print("go back")
