def getcount(g):
    l=[]
    for i in g:
        if i not in l:
            l.append(i)
    return l
g=[10,20,10,30,30,20]
l=(getcount(g))
print(len(l))

print("==============================================================")

def cdistinct(l):
    res=1
    for i in range(1,len(l)):
        if l[i] not in l[0:i]:
            res=res+1
    return res

l=[10,20,10,30,30,20]
print(cdistinct(l))

print("==============================================================")

def cdistinct(l):
    s=set(l)
    return len(s)
l=[10,20,10,30,30,20]
print(cdistinct(l))

print("==============================================================")

def cdistinct(l):
    return len(set(l))
l=[10,20,10,30,30,20]
print(cdistinct(l))
