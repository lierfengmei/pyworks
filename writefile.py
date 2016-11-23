#!/usr/bin/env python
# encoding: utf-8


"""
@version: 0.1
@author: MM
@license: MM's Licence 
@contact: balabala@gmail.com
@site: AllitWell
@software: PyCharm
@file: writefile.py
@time: 2016/11/22 16:38
"""

import os
ls = os.linesep

#input filename
while True:
    fname = input("Please input a file name:")
    if os.path.exists(fname):
        print("the file %s is already exists" % fname)
    else:
        break

#input writedatas
writedatas = []
print("Input contents by lines(input '.' to quit)")
while True:
    data = input(">  ")
    if data == '.':
        break
    else:
        writedatas.append(data)

#write datas to file
try:
    with open(fname,'w') as fobj:
        fobj.writelines(["%s %s" % (eachItem,ls) for eachItem in writedatas])
        fobj.close()
except IOError as err:
    print("File error",err)



if __name__ == '__main__':
    pass