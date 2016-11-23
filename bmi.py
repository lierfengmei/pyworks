import math
# 导入数据库

name = input('Please input your name: ')
weight = float(input('input your weight： '))
height = float(input('input your height：'))
bmi = weight/pow(height,2)
if bmi<18.5:
    print(name,'：你的BMI指数为%.2f,'%bmi,'过轻')
elif bmi<25:
    print(name,'：你的BMI指数为%.2f,'%bmi,'正常')
elif bmi<28:
    print(name,'：你的BMI指数为%.2f,'%bmi,'过重')
elif bmi<32:
    print(name,'：你的BMI指数为%.2f,'%bmi,'肥胖')
else:
    print(name,'：你的BMI指数为%.2f,'%bmi,'严重肥胖')