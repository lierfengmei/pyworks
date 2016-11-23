
#---------------------------------------------------
#摘要算法又称为哈希算法、散列算法。它通过一个函数，把任意长度的数据
#转换为一个长度固定的数据串（通常用16进制的字符串表示）

#import hashlib

# def calc_md5(password):
# 	md5 = hashlib.md5
# 	md5.update(password.encode('utf-8'))
# 	return get_md5(password+'the-Salt')
	#return md5.hexdigest()

# db = {
# 	 'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
#     }

# def login(username,password):
# 	pass

import hashlib 

db = {}

def get_md5(s):
	md5 = hashlib.md5()
	md5.update(s.encode('utf-8'))
	return md5.hexdigest()

def register(username,password):
	db[username] = get_md5(password+username+'the-Salt')


def login(username,password):
	if get_md5(password+username+'the-Salt')==db[username]:
		print('Login in successful!')
	else:
		print('Login in not successful!')

# 测试 Test		
if __name__=='__main__':
	register('Lucy','123456')
	register('Bob','fdjsoajfoa')
	register('Luna','808jflajlf')
	print(db)
	login('Lucy','123456')
	login('Lucy','fjlasj')
	login('Bob','fdjsoajfoa')

