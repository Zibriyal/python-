"""n=int(input("select operation :"))
a=int(input("enter first number"))
b=int(input("enter second number"))
if n==1:
    print("addition",a+b)
elif n==2:
    print("subtraction",a-b)

elif n==3:
    print("multiplication",a*b)
else:
    print("Invalid input")"""

import sys
print("""Please select operation:
1. Addition
2. Subtraction
3. Multiplication
""")
choice=int(input("Enter your choice from 1,2 Or 3 :"))
if choice not in (1,2,3):
    print("Invalid input")
    sys.exit()

a=int(input("enter first number"))
b=int(input("enter second number"))
if choice==1:
    res=a+b
elif choice==2:
    res=a-b
else:
    res=a*b
print("The result is :",res)