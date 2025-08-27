l1=[x for x in range(11) if x%2==0]
print(l1)

l2=[x for x in range(11) if x%2!=0]
print(l2)

print('-------------------------------------------------------')

#Function to get a list that contain all the items of l that are smaller than x

def getsmaller(l,x):
    return [e for e in l if e<x ]
l=[9,15,12,3,7,11]
x=10
print(getsmaller(l,x))

print('-------------------------------------------------------')

def getevenodd(l):
    even=[x for x in l if x%2==0]
    odd=[x for x in l if x%2!=0]
    return even,odd
l=[10,3,20,5,12]
even,odd=getevenodd(l)
print(even)
print(odd)

#example

s='geeksforgeeks'

l1=[x for x in s if x in 'aeiou']
print(l1)

l2=['geeks','ide','courses','gfg']
l3=[x for x in s if x.startswith('g')]
print(l3)

l4=[x*2 for x in range(6)]
print(l4)


print('-------------------------------------------------------')

l1=['geeks','for','geeks','gfg','ide']
l2=[x.upper() for x in l1 if x.startswith('g')]
print(l2)


print('---------------Set comprehension----------------------------------------')

l1=[10,20,3,4,10,20,7,3]

s1={x for x in l1 if x%2==0}
print(s1)
s2={x for x in l1 if x%2!=0}
print(s2)


print('-------------------------Dictionary comprehension------------------------------')

l1=[1,3,4,2,5]
d1={x:x**3 for x in l1}
print(d1)


d2={x:f'ID{x}' for x in range(5)}
print(d2)

l2=[101,103,102]
l3=['gfg','ide','course']
d3={l2[i]:l3[i] for i in range(len(l2))}
print(d3)

#Inverting a dictionary (key becomes value and value becomes key)
d1={101:'gfg',102:'ide',103:'course'}
d2={v:k for k,v in d1.items()}
print(d2)

