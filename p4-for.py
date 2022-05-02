'''字符串是可迭代的 
for循环:
for 变量 in 可迭代的东西：
代码
把可迭代的东西中每一项拿出来，挨个的赋值给变量'，每一次赋值都要执行一次循环代码
for 循环想要计数,必须要借助range
range(n)从0-n,不包含n
range(m,n)m=<,<n
range(m,n,s)从m数到n,不包括n,间隔为s'''
for i in range(1,10,2):
    print(i)

'''pass:代码占位'''
a = 1 
if a > 10:
    pass #没想好条件的设置，先过，不破坏代码的完整性


