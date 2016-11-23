# -*- coding:utf-8 -*-



# global_dict = {}

# def student_thread(name):
# 	std = Student(name)
# 	global_dict[threading.current_thread()] = std
# 	do_task_1()
# 	do_task_2()

# def do_task_1():
# 	std = global_dict[threading.current_thread()]

# def do_task_2():
# 	std = global_dict[threading.current_thread()]




# def process_student(name):
# 	std = Student(name)
# 	#std 是全局变量，但是每个函数都需要调用它
# 	do_task_1(std)
# 	do_task_2(std)


# def do_task_1(std):
# 	do_subtask_1(std)
# 	do_subtask_2(std)

#---------------------------------------------------------
# ThreadLocal

import threading

#创建全局ThreadLocal变量
local_school = threading.local()

def process_student():
	std = local_school.student
	print('Hello,%s in (%s)' % (std,threading.current_thread().name))

def process_thread(name):
	#绑定ThreadLocal的student
	local_school.student = name
	process_student()


t1 = threading.Thread(target = process_thread,args = ('Alice',),name = 'Thread-A')
t2 = threading.Thread(target = process_thread,args = ('Bob',),name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
print('Threads ended')