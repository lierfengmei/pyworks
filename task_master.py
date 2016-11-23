# task_master.py

import time,random,queue

from multiprocessing managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()

#接收结果的队列
result_queue = queue.Queue()

#从BaseManager继承的QueueManager

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue',callable = lambda:task_queue)
QueueManager.register('get_result_queue',callaable = lambda:result_queue)

manager = QueueManager(address = ('',5000), authkey = b'abc')
manager.start()
