# -*- coding:utf-8 -*-

def is_palindrome(n):
	n = list(str(n))
	if(n[::1]!=n[::-1]):
		return False
	return True


output = filter(is_palindrome,range(1,100))
print(list(output))