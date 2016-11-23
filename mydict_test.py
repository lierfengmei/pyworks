# -*- coding:utf-8 -*-

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

	def setUp(self):
		print('setUp……')

	def tearDown(self):
		print('tearDown……')

	def test_init(self):
		d = Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key,'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']
	#这个意思是，通过d['empty']访问不存在的key的时候，
	#断言会抛出keyError

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
	#而通过d.empty访问不存在的key时，我们期待抛出
	#AttributeError


	#运行单元测试

if __name__ == '__main__':
	unittest.main()



def abs(n):
	'''
	Function to get absolute value of number.
	Example:
	>>>abs(1)
	1
	>>>abs(-1)
	1
	>>>abs(0)
	0
	'''
	return n if(n>=0) else(-n)


