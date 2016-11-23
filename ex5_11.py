#!/usr/bin/env python
# encoding: utf-8


"""
@version: 0.1
@author: MM
@license: MM's Licence 
@contact: balabala@gmail.com
@site: AllitWell
@software: PyCharm
@file: ex5_11.py
@time: 2016/11/23 9:02
"""
#1）使用循环和算术运算，求出0~20之间所有的偶数

def calEven():
    print()
    print("Even numbers between 0~20 are:")
    for eachNum in range(20):
        if eachNum%2==0:
            print(eachNum," ",end = "")

def calOdd():
    print()
    print("Odd numbers between 0~20 are:")
    for eachNum in range(20):
        if eachNum%2==1:
            print(eachNum," ",end = "")

def calDivide():
    print()
    num1 = int(input("Please input one number:"))
    num2 = int(input("Please input another number:"))
    if (not num1) and (not num2):
        print("two numbers are all zeros!")
        return False
    elif (not num1) or (not num2):
        print("是的，它们有整除关系")
        return True
    elif (not num1%num2) or (not num2%num1):
        print("是的，它们有整除关系")
        return True
    else:
        print("不，它们没有整除关系")
        return False

if __name__ == '__main__':
    calEven()
    calOdd()
    calDivide()
