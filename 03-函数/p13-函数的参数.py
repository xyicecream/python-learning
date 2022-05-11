'''
参数： 可以在函数调用的时候，给函数传递一些信息

分类：
   1.形参：在函数定义的时候，需要 定义一些变量来接受信息
      1.位置参数，按照位置一个一个的去声明变量
      2.默认值参数，在函数声明的时候给变量一个默认值，如果实参不传递信息，此时默认值生效，否则就不生效
      3.动态传参
        1. *args ，表示接收的所有的位置参数的动态传参
        2. **kwargs, 表示接收所有的关键字的动态传参

      顺序：位置参数 > *aegs > 默认值参数 > **kwargs
      位置参数放在前面，默认值参数放在后面
   2.实参：实际在调用的时候传递的信息
      1.位置参数，按照位置传参
      2.关键字传参，按照参数的名字来传参
      3.混合传参
        顺序：位置参数放前面，关键字参数放后面 否则报错
    实参在执行的时候，必须要保障形参有数据。
'''
# # 1.骂谁 ？ 2.骂到什么程度
# def maren(ren,lvl): # 形参
#     print("1.怒",ren)
#     print("2.验证",ren)
#     if lvl > 99:
#         print("3.不要脸")
#     else:
#         print("3.搞什么")
#     print("4.结束")

# maren("sb居委",999) # 在调用函数的时候，才能知道到底骂谁， -> 实参

# # 写一个计算器，可以实现+-*/运算
# def cal(a,opl,b):
#     if opl == "+":
#         print(a+b)
#     elif opl == "-" :
#         print(a-b)
#     elif opl == "*" :
#         print(a*b)
#     elif opl == "/" :
#         print(a/b)
#     else :
#         print("错误")
# cal(234,"+",789)

# cal(a = 199,opl = "*",b = 389)

def luru(name,age,gender = "男"):
    print(name,age,gender)

luru("jay",18)
luru("jio",20)
luru("anny",22,"女")

def chi(*food): # *表示位置参数的动态传参。*接受到的值会被统一放在一个元祖里面
    print(food)

chi("米饭","土豆丝","奶茶")
chi("果汁")


def eat(**food): # **表示关键字参数的动态传参。**接受到的所有会被统一放在一个字典里面
    print(food)

eat(zhu = "米饭",fu = "土豆丝",tian="奶茶")
#eat("果汁")

def func(*args, **kwargs):#没有任何限制的接收任何参数
    pass

lst = [111,222,333,444]
def func(*args):
    print(args)
func(*lst) # *在实参位置，是把列表变成位置参数进行传递
           # **在实参文职，把字典自动转化为关键字参数进行传递

