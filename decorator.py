
# # # def log(func):
# # # 	def wapper(*args,**kw):
# # # 		print('call %s:'% func.__name__)
# # # 		return func(*args,**kw)
# # # 	return wapper

# # # @log
# # # def now():
# # # 	print('2016-06-16')


# # # def log(func):
# # # 	def wapper(*args,**kw):
# # # 		print('call:%s'% func.__name__)
# # # 		return func(*args,**kw)
# # # 	return wapper

# # 此乃3层嵌套的decorator:
# # def log(text):
# # 	def decorator(func):
# # 		def wapper(*args,**kw):
# # 			print('%s,%s'%(text,func.__name__))
# # 			return func(*args,**kw)
# # 		return wapper
# # 	return decorator


# # @log('execute')
# # def now():
# # 	print('2016-06-16')


# # now = log('execute')(now)


# # import functools

# # def log(func):
# # 	@functools.wrap(func)
# # 	def wrapper(*args,**kw):
# # 		print('call %s:'% func.__name__)
# # 		return func(*args,**kw)
# # 	return wapper




# #编写decorator,能在函数调用的前后打印出‘begin call’和‘end call’的日志

# def log(func):
# 	def wapper(*args,**kw):
# 		print('begin call')
# 		return func(*args,**kw)
# 	#	print('end call')
# 	return wapper


# @log
# def now():
# 	print('now:2016-06-16 18:46')
import functools

def log(text = ''):
	def decorator(func):
		@functools.wraps(func)  #为啥呢？！
		def wrapper(*args,**kw):
			print('call begin %s %s'%(text,func.__name__))
			result =  func(*args,**kw)
			print('call end %s %s'%(text,func.__name__))
			return result
		return wrapper
	return decorator

@log('execute')
def now():
	print('2016-06-16')

now()

@log()
def now():
	print('2016-06-16')

now()

@log()
def now():
	print('2016-11-22')