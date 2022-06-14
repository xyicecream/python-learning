# 线程 -> 执行单位，进程 ->资源单位
# 一个进程里面，至少要有一个线程
# 启动每一个程序默认都会有一个主线程

# 这是个单线程的代码
# def func():
#     for i in range(1000):
#         print("func",i)
# if __name__ == '__main__': #函数是用来控制python文件执行的场景，使用该函数的最大作用就是为了控制该函数下面的语句在其他文件中导入时不执行效果。
#     func()
#     for i in range(1000):
#         print("main",i)

#实现多线程
# from threading import Thread #线程类
# def func():
#     for i in range(1000):
#         print("func",i)

# if __name__ == '__main__': #函数是用来控制python文件执行的场景，使用该函数的最大作用就是为了控制该函数下面的语句在其他文件中导入时不执行效果。
#     t = Thread(target=func) # 创建线程，并给线程安排任务 调用函数时子线程
#     t.start() #多线程状态为可以开始执行该线程，具体执行时间由CPU决定
#     for i in range(1000):# 主线程
#         print("main",i)

# 多个子线程
from threading import Thread #线程类
import time 
def func(name,delay):
    for i in range(100):
        time.sleep(delay)
        print(name,i)

if __name__ == '__main__':  # 有时间差才能看出来究竟是怎么跑的
    t1 = Thread(target=func,args=("xy",0.1,)) #传参必须是元组  # 创建线程，并给线程安排任务 调用函数时子线程
    t1.start() #多线程状态为可以开始执行该线程，具体执行时间由CPU决定
    t2 = Thread(target=func,args=("cc",0.2,)) #传参必须是元组  # 创建线程，并给线程安排任务 调用函数时子线程
    t2.start() 
    # for i in range(1000):# 主线程
    #     print("main",i)


#from threading import Thread


# class MyThread(Thread):
#     def run(self): # 固定的 当线程可以执行之后，被执行的就是run()
#         for i in range(100):
#             print("子线程",i)

# if __name__ == '__main__':
#     t = MyThread()
#     t.start() #开启线程
#     for j in range(100):
#         print("主线程",j)


# 多进程

# from multiprocessing import Process
# def func():
#     for i in range(1000):
#         print("子进程",i)

# if __name__ == '__main__':
#     t = Process(target = func)
#     t.start()
#     for i in range(1000):
#         print("主进程",i)

# import _thread
# import time

# 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# # 创建两个线程
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: 无法启动线程")

# while 1:
#    pass