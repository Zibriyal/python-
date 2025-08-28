def isSorted(l):
    i=1
    while i<len(l):
        if l[i]<l[i-1]:
            return False
        i+=1
    return True
l=[10,20,30,15,40]

if isSorted(l):
    print("Sorted list is sorted")
else:
    print("Sorted list is not sorted")


#MEthod 2 using sorted()
def isSorted(l):
    sl=sorted(l)
    if sl==l:
        return True
    else:
        return False

l=[10,20,30,15,40]
if isSorted(l):
    print("Sorted list is sorted")
else:
    print("Sorted list is not sorted")
