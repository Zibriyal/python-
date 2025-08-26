l=[10,20,30,40,50]

print(l[0:5:2])

print(l[:4])

print(l[2:])

print(l[1:4])

print(l[4:1:-1])

print(l[-1:-6:-1])

print(l[::-1])

print(l[0:5])

print(l[:])


l1=[10,20,30]
l2=l1[:]

t1=(10,20,30)
t2=t1[:]

s1='geeks'
s2=s1[:]

print(l1 in l2)
print(t1 in t2)
print(s1 in s2)