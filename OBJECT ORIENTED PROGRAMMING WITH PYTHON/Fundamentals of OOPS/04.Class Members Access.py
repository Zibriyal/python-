class Test:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fun(self):
        print('Hi')
t=Test(10,20)
print(t.x)
print(t.y)
t.fun()

print('________________________________________________________')

class Test:
    def __init__(self,x,y):
        self._x=x
        self.y=y

    def _fun(self):
        print('Hi')
t=Test(10,20)
print(t._x)
print(t.y)
t._fun()


print('________________________________________________________')

"""
class Test:
    def __init__(self,x,y):
        self.__x=x
        self.y=y

    def __fun(self):
        print('Hi')

t=Test(10,20)
print(t.__x)
print(t.y)
t.__fun()
"""
print('________________________________________________________')

class Test:
    def __init__(self,x,y):
        self.__x__=x
        self.y=y

    def __fun__(self):
        print('Hi')

t=Test(10,20)
print(t.__x__)
print(t.y)
t.__fun__()

print('________________________________________________________')

class Test:
    def __init__(self,x,y):
        self.__x=x
        self.y=y

    def __fun(self):
        print('Hi')

t=Test(10,20)
print(t._Test__x)
print(t.y)
t._Test__fun()

print('________________________________________________________')

class Test:
    def __init__(self,x):
        self.x=x
        self.__y=10
    def printTest(self):
        print(self.x)
        print(self.__y)
t=Test(5)
t.printTest()

print('________________________________________________________')

class Test:
    def __init__(self,x):
        self.x=x
        self.__y=10
    def printTest(self):
        print(self.x)
        print(self.__y)
t=Test(5)
t.printTest()
print(t.__y)              #Error