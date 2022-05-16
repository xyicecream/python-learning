'''
回顾：
   1.函数可以作为参数进行传递
   2.函数可以作为返回值返回
   3.函数名称可以当做变量进行赋值操作

装饰器：
    本质上是个闭包
    作用：
        在不改变原有函数调用的情况下，给函数增加新功能
        （在函数前后添加新的功能，但是不改变原来的代码）
    
    在用户登录的地方，日志
    通用装饰器：
       def wrapper(fn): wrapper:装饰器 fn:目标函数
           def inner(*args,**kwargs):
               #在目标函数执行前……
               ret = fn(*args,**kwargs)
               #在目标函数执行后……
               return ret
            return inner
        @wrapper
        def target():
            xxxxxx
        target() 实际上是inner() 

        一个函数可以被多个装饰器装饰
        @wrapper1
        @wrapper2
        def t():
            print("目标")
        规则和规律 : wrapper1 wrapper2 t wrapper2 wrapper1

'''
# 1.
# def func():
#     print("我是函数")

# def ggg(fn): # fn要求是个函数
#     fn() # 相当于fn()
# ggg(func) 

#2.
# def func():
#     def inner():
#         print(123)
#     return inner

# ret = func() #相当于ret = inner
# ret() #要知道ret是什么，直接调用

#3.
# def func1():
#     print(1)
# def func2():
#     print(2)

# func1 = func2
# func2()


# def guanjia(game):
#     def inner():
#         print("开外挂")
#         game()
#         print("关外挂")
#     return inner # 相当于返回了一个开外挂 玩游戏 关外挂的 包
    

# @guanjia #相当于 play_dnf = guanjia(play_dnf)
# def play_dnf():
#     print("玩游戏")
# @guanjia
# def play_lol():
#     print("阿巴阿巴")

# #play_dnf = guanjia(play_dnf) # 将游戏的新包重新赋值给老游戏
# play_dnf() # 其实运行的是inner


# 被装饰函数的参数问题
# def guanjia(game):
#     # *接收所有参数，打包成元组和字典
#     def inner(*args,**kwargs): #inner添加了参数，args一定是一个元祖，kwargs一定是字典
#         print("开外挂")
#         # *，** 表示把args 和 kwargs 打散成位置参数和关键字参数传递进去
#         game(*args,**kwargs)
#         print("关外挂")
#     return inner # 相当于返回了一个开外挂 玩游戏 关外挂的 包
    

# @guanjia #相当于 play_dnf = guanjia(play_dnf)
# def play_dnf(username,password):
#     print("玩游戏",username,password)
# @guanjia
# def play_lol(username,password,hero):
#     print("阿巴阿巴",username,password,hero)

# #play_dnf = guanjia(play_dnf) # 将游戏的新包重新赋值给老游戏
# play_dnf("xy","123456") # 其实运行的是inner
# play_lol("xy","123456","百里")


# #装饰器的返回值问题
# def guanjia(game):
#     # *接收所有参数，打包成元组和字典
#     def inner(*args,**kwargs): #inner添加了参数，args一定是一个元祖，kwargs一定是字典
#         print("开外挂")
#         # *，** 表示把args 和 kwargs 打散成位置参数和关键字参数传递进去
#         ret = game(*args,**kwargs)
#         print("关外挂")
#         return ret
#     return inner # 对guanjia相当于返回了一个开外挂 玩游戏 关外挂的 包
    

# @guanjia #相当于 play_dnf = guanjia(play_dnf)
# def play_dnf(username,password):
#     print("玩游戏",username,password)
#     return "一个"
# @guanjia
# def play_lol(username,password,hero):
#     print("阿巴阿巴",username,password,hero)

# #play_dnf = guanjia(play_dnf) # 将游戏的新包重新赋值给老游戏
# ret = play_dnf("xy","123456") # 其实运行的是inner
# play_lol("xy","123456","百里")
# print(ret)

# #一个函数可以被多个装饰器装饰
# def wrapper1(fn):
#     def inner():
#         print("w1,进入")
#         ret =  fn()
#         print("w1,出去")
#         return ret
#     return inner

# def wrapper2(fn):
#     def inner():
#         print("w2,进入")
#         ret =  fn()
#         print("w2,出去")
#         return ret
#     return inner

# @wrapper1
# @wrapper2
# def t():
#     print("目标")

# t()

#一个例子
log_flag = False
def log_verify(fn):
    def inner(*args,**kwargs):
        # 登录验证
        global log_flag
        if log_flag == False: #当是假，执行登录操作，否则执行下一步
            while True:
                username = input("...")
                password = input("...")
                if username=="admin" and password =="123":
                    print("登录成功")
                    log_flag =True
                    break
                else:
                    print("登录失败")
        ret = fn(*args,**kwargs)
        return ret
    return inner


@log_verify
def add():
    print("添加信息")

@log_verify
def dele():
    print("删除信息")

@log_verify
def upd():
    print("修改信息")

@log_verify
def search():
    print("搜索信息")

add()

