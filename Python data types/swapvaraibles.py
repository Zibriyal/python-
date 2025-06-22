x=100
y=200

temp=x
x=y
y=temp
print(x)
print(y)

#Second method
x,y= y,x
print(y)
print(x)


x,y,z= 100,'geeks',10.5
print(x)
print(y)
print(z)

x,y = x-5,y+'for'

print(x)
print(y)

print(id(5))
a=10
print(id(a))
b=a
print(id(b))
print('__________________________________________')

a=10
b=10

print(id(a))
print(id(b))

print('__________________________________________')

c='geeks'
d='geeks'

print(id(c))
print(id(d))

print('__________________________________________')


a=10
b=10
print(a is b)
c=a
print(c is b)
c=20
print(c is b)