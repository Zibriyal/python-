n=12
def dectobin(n):
    if n==0:
        return '0'
    res=''
    while n>0:
        res=res+str(n%2)
        n=n//2
    return res[::-1]
print(dectobin(n))
print('-------------------------------------------')
#Direct method
n=12
def dectobin(n):
    res=bin(n)
    return res[2:]
print(dectobin(n))