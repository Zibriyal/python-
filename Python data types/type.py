a=10
print(type(a))
b=10.5
print(type(b))
c=2+2j
print(type(c))

print('__________________________________________')


a= True
print(type(a))

b=None
print(type(b))

print('__________________________________________')


str='gfg'
print(type(str))

l=[10,20,30]
print(type(l))

s={10,20,30}
print(type(s))

t=(10,20,30)
print(type(t))

d={10:'gfg',20:'ide'}
print(type(d))
print('__________________________________________')


l=[10,20,30,40,50]
print(l)

print(l[3])
print(l[-1])
print(l[-2])

print(l)

l.append(30)

print(l)

l.insert(1,15)
print(l)

print(l.count(30))
print(l.index(30))
print(15 in l)

print(l.index(30,4,7))

print('__________________________________________')


l=[10,20,30,40,50,60,70,80]

l.remove(20)
print(l)
print('__________________________________________')
print(l.pop(1))
print(l)
print('__________________________________________')

print(l.pop(2))
print(l)
print('__________________________________________')

del l[1]
print(l)
print('__________________________________________')

del l[0:2]
print(l)
print('__________________________________________')

l=[10,40,20,50]

print(max(l))
print('__________________________________________')

print(min(l))
print('__________________________________________')

print(sum(l))
print('__________________________________________')

l.reverse()
print(l)
print('__________________________________________')

l.sort()

print(l)