#break 让当即循环立即停止
# while True:
#     content = input("please enter:")
#     if content == "q": # == 表示判断左右两端是否一致
#         break #结束循环
#     print ("sent to the following:",content)

#continue :停止当前本次循环，继续执行下一次
#从1数到10
i = 1 
while i <=10:
    if i == 4:
        i = i+1
        continue
    else: 
        print(i)
        i = i + 1 
