n=int(input("Enter a number: "))                        #91 , 101 ,21, -21

if (n<=1):
    print("Not a prime number")

else:
    for i in range(2,n):
        if n%i==0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
