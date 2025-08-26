b='1100'
def bintodec(b):
    res=0
    p=1
    for x in reversed(b):
        res=res+int(x)*p
        p=p*2
    return res
print(bintodec(b))

print('-----------------------------')

b='1100'
def bintodec(b):
    res=int(b,2)
    return res

print(bintodec(b))