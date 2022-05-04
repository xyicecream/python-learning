# #1.字符串的格式化
# # 我叫xxx，我住在xxx，我今年xxx岁，我喜欢xxx
# name = input("请输入你的名字：")
# address = input("请输入你的地址：")
# age = int(input("请输入你的年龄：")) #将字符串转化为整数
# hoby = input("请输入你的爱好：")
# #%s 字符串占位
# #%d 占位整数 %f 占位小数
# s = "我叫%s,我住在%s，我今年%d岁，我喜欢%s" %(name,address,age,hoby)
# s1 = "我叫{},我住在{}，我今年{}岁，我喜欢{}".format(name,address,age,hoby)
# s2 = f"我叫{name},我住在{address}，我今年{age}岁，我喜欢{hoby}" #f-string
# print(s2)

#2.索引和切片
# 按照位置提取元素
# s = "我叫周杰伦" 
#采用索引的方式提取某个字符
# print (s[3]) #编程是从0开始数数
# print (s[0])
# print (s[-1]) #-表示倒数

# #切片：从一个字符串中提取一部分内容
# s = "我叫周杰伦，你呢？你叫周周吗？"
# print (s[3:6]) #从索引3位置进行切片，切到6结束，不包括6
# # 语法：s[start,end] 从start到end进行切片，但是取不到end
# print(s[:5]) #如果start是从开头进行切片，可以省略
# print(s[6:]) #从start开始一直截取到结尾
# # ： 如果左右两端都是空白，表示开头或者结尾
# print(s[:])
# print(s[-3:-1]) #还是从左到右切片

# s = "我爱你"
# # 给切片添加步长来控制切片的方向
# print(s[::-1]) #-表示从右往左

# #语法：s[start:end:step] 从start切到end，每step个元素出来一个元素

# s = "ABCDEFGHIJKLMNOPQRST"
# print(s[3:8:2])
# print(s[-1:-10:-3])

#3.1字符串常规操作
#字符串的操作一般不会对原字符串产生影响，一般是返回一个新的字符串
# s = "python"
# s1 = s.capitalize()
# print(s1)

# s = "I have a dream!"
# s1 = s.title() #单词的首字母大写
# print(s1)

# s = "I HAVE A DREAM"
# s1 = s.lower() #把所有字母变成小写
# print(s1)

# s = "i have a dream"
# s2 = s.upper() #把所有字母变成大写
# print(s2)

#如何忽略大小写来进行判断 upper 重点
# verify_code = "aFH1"
# user_input = input(f"请输入验证码（{verify_code}）:")
# if user_input.upper() == verify_code.upper():
#     print("验证码正确")
# else:
#     print("验证码错误")

# 3.2 替换和切割
# strip() 去掉字符串左右两端的空白符（空格，\t,\n）
# s = "  你好， 我 叫 周杰伦  "
# s1 = s.strip()
# print (s1)

# #案例
# username = input("请输入用户名：").strip()
# password = input("请输入密码：").strip()
# if username == "admin":
#     if password == "123456":
#         print("登录成功")
#     else:
#         print("登录失败")
# else:
#     print("登录失败")

# #字符串替换 replace(old,new)
# s = "你好呀，我叫CC"
# s1 = s.replace("CC","icecream")
# print(s1)

# a = "i love icecream"
# a1 = a.replace(" ","") #去掉所有空格
# print(a1)

# #split() 字符串的切割
# b = "python_java_c_c#_javascript"
# lst = b.split("_") #切割之后的结果会放在列表中
# print(lst)
# lst2 = b.split("_java_")
# print(lst2)

#总结，replace(),strip(),split()

# ==========================================
#3.4 字符串的查找和判断
#查找
s = "你好啊，我是周润发"
ret =  s.find("周润发123") #返回值是-1就是没有该字符串出现
print(ret)
# ret2 = s.index("zgh") #如果报错就没有
# print(ret2)
print("周润发" in s) # in可以做条件上的判断
print("周润发" not in s) #not in判断是否不存在

#判断
name = input ("请输入你的名字：")
#判断你是不是姓张
if name.startswith("张"): #判断字符串是否以XXX开头，endswith 以XXX结尾
    print("你姓张")
else:
    print("你不姓张")

money = input("请输入你的钱：")
if money.isdigit():#判断字符串是否由整数组成,isdecimal检查字符串是否只包含十进制字符
    print("可以花钱")
else:
    print("您输入有误")

#总结 startswith(),isdigital(),in, not in

#=============
#3.5 补充和总结
#len()字符串长度
print(len("hello"))

#join()
lst3 = ["aaa","bbb","ccc"]
# 用_把上面的字符串连起来
c = "_".join(lst3)
print(c)
 

###总结：重点
'''
1. f"{变量}" 格式化一个字符串
2.索引和切片
 索引：从0开始的，【】
 切片：s[start:end:step],end位置的数据永远拿不到
3.相关操作：
  字符串的操作永远不会改变原字符串
  1.upper() 在需要忽略大小写的时候
  2.strip() 去除左右两端的空白（空格，\t,\n）
  3.replace() 字符串替换
  4.split() 对字符串进行切割，存储到一个列表中
  5.join() 将列表中的内容拼接为一个新的字符串
  6.startswith() 判断字符串是否以xx为开头
  7.len() 字符串长度（内置函数）

字符串的循环和遍历
for c in s:
    print(c) 字符串中的每一个字符

关于in：
    1.判断xxx是否在xxx中出现了
    2.for循环
'''
