
#!/usr/bin/python3
# -*- coding=utf-8 -*-
# Create by zhangxg
# from datetime import datetime
# import sched
# import time
#
# '''
# 每个 10 秒打印当前时间。
# '''
#
#
# def timedTask():
#     # 初始化 sched 模块的 scheduler 类
#     scheduler = sched.scheduler(time.time, time.sleep)
#     # 增加调度任务
#     scheduler.enter(10, 1, task)
#     # 运行任务
#     scheduler.run()
#
#
# # 定时任务
# def task():
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#
#
# if __name__ == '__main__':
#     timedTask()


import time
import schedule
import datetime

def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time :',ts)

def func2():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time：',ts)


def tasklist():
 #创建一个按秒间隔执行任务
    schedule.every(1).seconds.do(func)
 #创建一个按2秒间隔执行任务
    schedule.every(2).seconds.do(func2)
 #执行10S

for i in range(10):
     schedule.run_pending()
     time.sleep(1)
     tasklist()
schedule.clear()
