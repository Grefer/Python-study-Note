# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:10:19 2019

@author: Admin
"""
#task_master.py
import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

#发送任务的队列
task_queue = queue.Queue()

#接收结果的队列
result_queue = queue.Queue()

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

#windows环境下绑定调用接口不能使用lambda，所以先定义函数
def get_task():
    return task_queue
def get_result():
    return result_queue
def test():
    
    #把两个Queue都注册到网络上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue',callable=get_task)
    QueueManager.register('get_result_queue',callable=get_result)
    
    #绑定端口5000，设置验证码’abc‘
    manager = QueueManager(address=('127.0.0.1',5004),authkey=b'123')
    #启动Queue
    manager.start()
    #获得通过网络访问的Queue对象
    try:
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        #放几个任务进去
        for i in range(10):
            n = random.randint(0,10000)
            print('Put task %d...' %n)
            task.put(n)
        #从result队列读取结果
        print('Try get result...')
        for i in range(10):
            r = result.get(timeout=10)
            print('Result:%s'%r)
    except:
        print('Manager error')
    finally:   
        #关闭
        manager.shutdown()
        print('master exit.')

#使用freeze缓解多线程爆炸的问题
if __name__ == '__main__':
    freeze_support()
    test()