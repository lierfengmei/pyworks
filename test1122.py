
'''
try:
    filename = input("Please input the file name:")
    fobj = open(filename,'r')
    for eachLine in fobj:
        print(eachLine,end="")
    fobj.close()
except IOError as e:
    print("File open error",e)
'''
'''
try:
    filename2 = input("Please input the file name:")
    with open(filename2,'r') as file:
        for eachLine in file:
            print(eachLine,end="")
except IOError as err:
    print("File open error",err)


class FooClass(object):
    "my very first class:FooClass"
    version = 0.1
    def __init__(self,nm = 'Jone Doe'):
        """constructor"""
        self.name = nm
        print("Create a class instance for %s" % self.name)
    def showname(self):
        print("Your name is %s" % self.name)
        print("My name is %s" % self.__class__.__name__)
'''


def printOrder(a,b,c):
    """function: print the a b c order if a<=b<=c"""
    if int(a)<=int(b)<=int(c):
        print("The sequence is %d %d %d" % (int(a),int(b),int(c)))
        return True
    else:
        return False

def sort3():
    """function: input 3 data and the order them"""
    a = input("Please input the first data:")
    b = input("Please input the second data:")
    c = input("Please input the third data:")
    if printOrder(a,b,c):
        return
    if printOrder(a,c,b):
        return
    if printOrder(b,a,c):
        return
    if printOrder(b,c,a):
        return
    if printOrder(c,a,b):
        return
    if printOrder(c,b,a):
        return

sort3()













