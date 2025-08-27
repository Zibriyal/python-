def getsmaller(l,x):
    result=[]
    for e in l:
        if e<x:
            result.append(e)
    return result
l=[8,100,20,40,3,7]
x=10
print(getsmaller(l,x))