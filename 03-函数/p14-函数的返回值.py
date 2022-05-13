'''
函数的返回值：函数执行后，会给调用方一个结果，这个结果就是返回值

关于return：
函数只要执行到了return，函数就回立即停止并返回内容，函数内的return的后续代码不会执行
   1.如果函数里面没有return，此时外界收到的是none
   2.如果写了return
     1.只写了return，后面不跟数据，此时接收到的依然是none
     2.return 值，表示函数有一个返回值
     3.return 值1，值2，值3，……，函数有多个返回值，外界收到测试项

'''

def func():
    return 1,2,3,4
ret = func()
print(ret)