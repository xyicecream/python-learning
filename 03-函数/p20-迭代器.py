'''
for 变量 in 可迭代：
  pass

iterable: 可迭代的
str, list, dict, tuple,set,open()

可迭代的数据类型都会提供一个叫迭代器的东西，这个迭代器可以帮我们把数据类型中的所有数据逐一的拿到

获取迭代器的两种方案：
   1.iter()内置函数可以直接拿到迭代器
   2.__iter()__  特殊方法

从迭代器中拿到数据：
   1.next() 内置函数
   2.__next__() 特殊方法

for里面一定是要拿迭代器的，所以所有不可迭代的东西不能用for循环

for循环一定会有next()出现

总结：迭代器统一了不同数据类型的遍历工作

迭代器本身也是可迭代的
迭代器本身的特性：
  1.只能向前，不能反复
  2.特别节省内存
  3.惰性机制
'''

# it = iter("你好呀，我是哈哈哈")
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))  # StopIteration  迭代停止

# it = "呵呵哒".__iter__()
# print(it.__next__())
# print(it.__next__())

# 模拟for循环工作原理
s = "我是xxxxxx"
it = s.__iter__()
while 1:
    try:  #异常处理
        data = it.__next__()
        print(data)
    except StopIteration:
        break


