"""n=int(input("Enter n:"))

res=1

for i in range(2,n+1):

    res=res*i

print("Factorial is :",res)"""


# Using inbuilt library function
import math

n=int(input("Enter n:"))

res= math.factorial(n)

print("The factorial is :",res)