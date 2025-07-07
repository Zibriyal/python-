n=int(input("Enter a number"))
"""
x=1
while x*x < n:
    if n%x==0:

        print(x,n//x)
    x=x+1
if x*x==n:
    print(x)
    
"""
#PRime checking OPtimized
if n<=1:
    print("Not a prime number")

else:
    x=2
    while x*x <= n:
        if n%x==0:
            print("Not a prime number")
            break
        x=x+1
    else:
        print("Prime number")
        