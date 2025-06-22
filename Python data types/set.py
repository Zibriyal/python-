s={10,20}
print(s)
s.add(30)
print(s)
s.add(30)
print(s)
s.update([40,50])
print(s)
s.update({60,70},[80,90])
print(s)


print('__________________________________________')

s={10,30,20,40}
s.discard(30)
print(s)
s.remove(20)
print(s)
s.clear()
print(s)
s.add(50)
del s

print('__________________________________________')


s={10,30,20,40}
print(len(s))
print(20 in s)
print(50 in s)

print('__________________________________________')


s1={2,4,6,8}
s2={3,6,9}

#Union operator
print(s1 | s2)
print(s1.union(s2))

#intersection
print(s1 & s2)
print(s1.intersection(s2))

#difference

print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)
print(s2.difference(s1))

#symmetric diff operator

print(s1 ^ s2)
print(s1.symmetric_difference(s2))

print('__________________________________________')

s6={2,4.1,6,8.1}
s7={4,8}

s1={2,4,6,8}
s2={4,8}
#isjoint
print(s6.isdisjoint(s7))
print(s1.isdisjoint(s2))
print('__________________________________________')

#issubset

print(s1.issubset(s2))  #All elements of s1={2,4,6,8} are not in s2={4,8}
print(s2.issubset(s1))  #All elements of s2 are in s1
print('__________________________________________')

#proper set

print(s1 < s2)

print(s2 < s1)
print('__________________________________________')

#super set

print(s1 >= s2)
print(s2 >= s1)
print('__________________________________________')

#proper subset

print(s1 > s2)

print(s2 > s1)