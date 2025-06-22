d={110:'abc',101:'xyz',102:'bcz',103:'abc'}
print(d)
print('__________________________________________')

d={}
d['laptop']=40000
d['mobile']=15000
d['earphone']=1500
print(d)
print(type(d))

print('__________________________________________')

#get() function

d={110:'abc',101:'xyz',102:'bcz',103:'abc'}
print(d.get(101))
print(d.get(125))
print(d.get(125,'NA'))

if 125 in d:
    print(d[125])
else:
    print('NA')

print('__________________________________________')

d={110:'abc',101:'xyz',102:'bcz',105:'pqr'}
print(d)
print('__________________________________________')

d[101]='wxy'
print(d)
print('__________________________________________')

print(d.pop(105))
print(d)
print('__________________________________________')

del d[102]
print(d)
print('__________________________________________')

d[108]='cbz'
print(d)

print('__________________________________________')

print(d.popitem())

print(d)


x=4
print(id(x))
print(id((int)(x+"GFG")))
