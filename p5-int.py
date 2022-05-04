#int 整数，加减乘除、大小比较；在某个特定区间内表示很清楚
#float:小数，浮点数；小数：数据范围是无限的
#计算机是二进制的：0，1；表示一个小数是有误差的

#bool:用来做条件判断
#取值范围：True False 

#基础数据类型直接的转化
a = 10  #在Python中，所有非0数字都是True，0是False
b = bool(a)
print(type(b))
print(b)

while 1: #死循环，恒为真
     print("aaa")

s= "string" #在Python中，所有的非空字符串都是true，空字符串是false
print(bool(s))
#在Python基本数据类型中，表示空的东西为false，表示不为空的东西是True

while 1:
    content = input("请输入：")
    if content: #content不为空，继续；为空，停止循环
        print("发送:",content)
    else:
        break