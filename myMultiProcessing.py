

# import os

# print('Process (%s) start...' % os.getpid())

# #only works on Unix/Linux/Mac:

# pid = os.fork()
# if pid==0:
# 	print('I am a child process(%s) and my parent is %s.' % (os.getpid(),os.getppid()))
# else:
# 	print('I(%s) just created a child process(%s)' % (os.getpid(),pid))


# 有可fork调用，一个进程在接到新任务时候就可以复制一个子进程来处理新任务。
# 常见的Apache服务器就是由父进程监听窗口，每当有新的http请求时，就fork出子进程
# 来处理新的http请求。

# 跨平台版本的多进程模块：multiprocessing   Process class

#-----------------------------------------------------------------------------------------------

# from multiprocessing import Process
# import os

# #子进程要执行的代码
# def run_proc(name):
# 	print('Run child process %s(%s) ' % (name,os.getpid()))

# if __name__ == '__main__':
# 	print('Parent process %s.'% os.getpid())
# 	p = Process(target = run_proc, args = ('test',))
# 	print('Child process will start')
# 	p.start()
# 	p.join()			#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
# 	print('Child process end.')


#---------------------------------------------------------------------------------------------------
#Pool
#批量的方式启动大量的子进程，采用进程池的方式批量创建：

# from multiprocessing import Process
# import os 
# from multiprocessing import Pool
# import time,random

# def long_time_task(name):
# 	print('Run task %s(%s)' % (name,os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random()*3)
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds' % (name,(end-start)))

# if __name__ == '__main__':
# 	print('Parent Process %s.' % os.getpid())
# 	p = Pool(4)
# 	for i in range(5):
# 		p.apply_async(long_time_task,args=(i,))
# 	print('Waiting for all subprocesses done...')
# 	p.close()
# 	p.join()
# 	print('All subprocesses done!')

#--------------------------------------------------------------------
#subprocess 模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出

# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# prin          t('Exit code:',r)


# import subprocess

# print('$nslookup')
# p = subprocess.Popen(['nslookup'],stdin = subprocess.PIPE,stdout= subprocess.PIPE,stderr= subprocess.PIPE)
# output,err = p.communication(b'set q=mx\n python.org\n exit\n')
# print(output.decode('utf-8'))
# print('Exit code:',p.returncode)


#--------------------------------------------------------
#进程间通信

from multiprocessing import Process,Queue
import os,time,random

#写数据进行执行的代码
def write(q):
	print('Process to write:%s' % os.getpid())
	for value in ['A','B','C']:
		print('put %s to queue' % value)
		q.put(value)
		time.sleep(random.random())

#读数据进程执行的代码
def read(q):
	print('Process to read:%s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue' % value)

if __name__ == '__main__':
	#父进程创建Queue，并传给各个子进程
	q = Queue()
	pw = Process(target = write,args = (q,))
	pr = Process(target = read,args = (q,))
	#启动子进程进入pw，写入:
	pw.start()
	#启动子进程进入pr,读出：
	pr.start()
	#等待pw结束
	pw.join()
	#pr进程是死循环，无法等待其结束，只能强行终止
	pr.terminate()
	