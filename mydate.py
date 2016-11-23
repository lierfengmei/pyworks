import re
from datetime import timezone,datetime,timedelta


def to_timestamp(dt_str,tz_str):
	
	dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')

	s = re.match(r'^UTC([+|-]\d{1,2}):00$',tz_str).group(1)

	
	#s = ''.join(s)

	tz = timezone(timedelta(hours = int(s)))

	dt = dt.replace(tzinfo = tz)

	return dt.timestamp()


import re
from datetime import timezone,timestamp,timedelta

def to_timestamp(dt_str,tz_str):
	dt = datetime.strptime(dt_str,'%Y-%m-%d %H-%M-%S')
	s = re.match(r'^UTC([+|-]\d{1,2}):00$',tz_str).group(1)
	tz = timezone(timedelta(hours = int(s)))
	dt = dt.replace(tzinfo = tz)
	return dt.timestamp()












# def to_timestamp(dt_str,tz_str):
# 	#先把日期转化为datetime
# 	dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')

# 	#解析时区信息，使用正则式提取时区信息
# 	str = re.match(r'^UTC([+|-]\d{1,2}):00$',tz_str).group(1)
# 	# print(str)
# 	# print(type(str))
# 	# str = ''.join(str)
# 	# print(str)
# 	# print(type(str))
# 	tz = timezone(timedelta(hours = int(str)))

# 	#为datetime设置timezone
# 	dt = dt.replace(tzinfo = tz)

# # 	return dt.timestamp()

if __name__ == '__main__':
	#测试
	t1 = to_timestamp('2015-6-1 08:10:30','UTC+7:00')
	assert t1==1433121030.0, t1

	t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
	assert t2 == 1433121030.0, t2

	print('PASS')