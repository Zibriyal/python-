"""def fun():
    a=10
    b=20
    print(a,b,c,d)

c=30
d=40
fun()
print(c,d)"""

def fun():
    x=10

x=15
fun()
print(x)

print('-------------------------------------------')

def fun():
    global x
    x=10

x=15
fun()
print(x)

print('-------------------------------------------')

def fun():
    y=x+5
    print(y)

x=15
fun()

print('-------------------------------------------')

"""def fun():
    x=x+5
    print(x)

x=15
fun()
"""
print('-------------------------------------------')


def fun():
    x=10
    globals()['x']=20
    print(x)

x=15
fun()
print(x)