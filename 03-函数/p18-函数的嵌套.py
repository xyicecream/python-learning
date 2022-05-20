'''
函数可以嵌套函数

1.函数可以作为返回值进行返回
2.函数可以作为参数进行互相传递
'''

# def func1():
#     b = 20
#     def func2(): #函数的嵌套，局部变量
#         pass
#     print(b)
#     func2() #局部访问

def func():
    def inner():
        print(123)
    return inner # 返回值是一个函数

b1 = func() # b1 是 func内部的inner,此时我们把一个函数当成一个变量进行返回的
b1()


