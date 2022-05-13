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
print(all([12,"呵呵","路"])) #当成and来看 true and true and true
print(any([0,123,""])) #当成or来看

#enumerate
lst = ["一二","布布","小喵","小基"]
for index,item in enumerate(lst):
    print(index,item)
for i in range(len(lst)):
    print(i,lst[i])

s = "xixi"
print(hash(s)) # 一定是一个数字，想办法转化成内存地址，然后进行数据的存储 -> 字典（集合）哈希表

# dir 当前这个数据能执行哪些操作






