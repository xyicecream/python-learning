'''
作用域：变量的访问权限

'''
a = 10 #全局变量 -> 全局作用域
print(a)

def func(): #全局函数
    b = 20  # 局部变量 -> 局部作用域
    print(a)

func()

def func3():
    c = 10086
    return c # 如果想要在函数外面访问，要用return
c1 = func3()
print(c1)