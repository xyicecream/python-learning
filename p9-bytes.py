'''
1. 字符集和编码
0 1 <=> 1010101010 <=>二进制转化 => 
电脑如何进行存储文字信息
ascii 码 编排了128个文字符号，只需要7个0和1就可以表示了，01111111 => byte => 8bit

ANSI => 一套标准，每个字符 16bit 2byte
00000000 01111111
中国，gb2312国标，gbk编码（Windows默认编码）， 又扩展了，
每个国家标准都不一样，不通用

Unicode:万国码
早期Unicode空间小，不够，2个byte
后来扩充， 4个字节

utf: 可变长度的unicode，可以进行数据的传输和存储
utf-8: 最短的字节长度
     英文：8bit，1byte
     欧洲文字：16bit，2byte
     中文：24bit，3byte
utf-16: 最短的字节长度16

总结：
   1. ascII 8bit 1byte
   2.gbk 16bit 2byte
   3.unicode 32bit 4byte 没法用一个标准
   4.utf：
    英文：8bit，1byte
    欧洲文字：16bit，2byte
    中文：24bit，3byte
    
gbk和utf-8 不能直接进行转化

'''
s = "周杰伦"
bs1 = s.encode("gbk") #编码
bs2 = s.encode("utf-8")
print(bs1) # b'xxxx' bytes类型
print(bs2)

# 怎么把一个gbk的字节转化成utf-8的字节
bs = b'\xd6\xdc\xbd\xdc\xc2\xd7'
#先把gbk转化成一个字符串
s1 = bs.decode("gbk") #解码
bs3 = s1.encode("utf-8") #编码
print(bs3)

# 1. str.encode("编码")
# 2. bytes.decode("解码")

#英文可以直接输出