'''
1.找到文件，双击打开
open(文件路径,mode = "",encoding = "")
    文件路径：
       1.绝对路径
       2.相对路径
         相对于当前你的程序的所在的文件夹

         ../ 上一层文件夹
    mode:
        r: read: 读取
        w: write:写入文件
        a: append 追加写入
        b: 读写的是非文本文件 bytes
    with: 上下文，不需要手动关闭一个文件
        
'''
import os # 和操作系统相关的模式导入
import time #和时间相关的

# f = open("xxx.txt",mode = "r",encoding = "utf-8") #要打开的文件xxx.txt和代码文件在一个文件夹
# #open(../a.txt) # 文件在外面的一个文件夹
# content = f.read() #内容
# line = f.readline() # 一行一行读文本中的内容
# line = f.readline().strip() #每一行末尾自带换行符\n,strip去除空白内容
# lines = f.readlines() 读出文本中每行的内容，并储存到一个列表里

#最重要的一种文本读取方式
# for line in f: #从F中读取每一行
#     print(line.stip())

# 写入文件
# W模式下，如果文件不存在，自动创建一个文件
# w模式下，每一次open，都会清空掉文件的内容
# f=open("学习.txt",mode = "w",encoding = "utf-8")
# f.write("累")
# f.close() #每次操作后都关闭链接

# 准备一个列表，把列表中的每一项内容，写入文件中
# lst = ["张无忌","赵敏","章子怡","汪峰"]
# f = open("小说.txt",mode = "w",encoding="utf-8")# 大多数情况下要把open卸载循环外面
# for item in lst:
#     f.write(item)
#     f.write("\n")
# f.close()

# #a模式
# f = open("小说.txt",mode = "a",encoding="utf-8")
# f.write("周芷若")

# with
with open("小说.txt",mode = "r",encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# 想要读取图片
#在读写非文本文件的时候模式加上b
# with open ("xxx.jpg",mode = "rb") as f:

#文件的复制
#从源文件中读取内容，写入到新路径去
# with open("1.jpg",mode = "rb") as f1,\
#      open("../2.jpg",mode = "wb") as f2:
#     for line in f1:
#         f2.write(line)


# 文件修改操作
# 把文件中的周->张
with open("小说.txt",mode = "r",encoding="utf-8") as f1,open("小说_副本.txt",mode = "w",encoding="utf-8") as f2:
    for line in f1:
        line = line.strip() #去掉换行
        if line.startswith("周"):
            line = line.replace("周","张") #修改 字符串不可修改，要重新赋值
        f2.write(line)
        f2.write("\n")
time.sleep(3) #程序休眠3s，再跑
#删除源文件
os.remove("小说.txt")
time.sleep(3)
#将副本文件重命名为源文件
os.rename("小说_副本.txt","小说.txt")