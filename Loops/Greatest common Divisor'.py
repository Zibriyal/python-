#To find out greatest common divisor for a and b
#The GCD of two numbers is the largest number that divides both of them without leaving a remainder.

"""a=int(input("Enter a:"))
b=int(input("Enter b:"))

small=min(a,b)

for i in range(1,small+1):
    if (a%i==0 and b%i==0):
        gcd=i

print("GCD is",gcd)

"""
#using inbuilt library function

import math
a=int(input("Enter a:"))
b=int(input("Enter b:"))
gcd=math.gcd(a,b)
print("GCD is :",gcd)