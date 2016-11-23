

import re
if re.match(r'^\d{3}\-\d{3,8}$','010-12345'):
	print('OK')
else:
	print('failed')

if re.match(r'^\d{3}\-\d{3,8}$','010 12345'):
	print('OK')
else:
	print('failed')


m = re.match(r'^(\d{3})-(\d{3,8})$','010-1234567')
print(m) 
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:25:30'
m = re.match(r'^([0-1][0-9]|2[0-3]|[0-9])\:([0-5][0-9])\:([0-5][0-9])$',t)
print(m.groups())

print(re.match(r'^(\d+)(0*)$','102300').groups())


print(re.match(r'^(\d+?)(0*)$','1023000').groups())



import re

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

print(re_telephone.match('010-122456').groups())

print(re_telephone.match('010-8086').groups())

t = re_telephone.match('010-1233332')

for i in range(3):
	print(t.group(i))


d = re.match(r'^([0-9a-zA-Z\.]+)\@([a-zA-Z]+)\.(com|org)$','bill.gates@microsoft.org')
#if(re.match(r'^([0-9a-zA-Z\.]+)\@([a-zA-Z]+)\.com$','someone@gmail.com')):
if d:
	print('Email match ok')
	print(d.groups())
else:
	print('Email match failed')




def to_timestamp(dt_str,tz_str):
	#先把日期转化为datetime
	dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')

	#解析时区信息，使用正则式提取时区信息
	tz = timezone(timedelta(hours = int(''.join(re.match(r'^UTC[\+|\-](\d{1,2})$',tz_str).groups())))

	#为datetime设置timezone

	dt = dt.replace(tzinfo = tz)

	return dt.timestamp()