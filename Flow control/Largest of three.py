#1) Excercise

"""a=int(input("ENter first number:"))
b=int(input("ENter second number:"))
c=int(input("ENter third number:"))

if a>b and a>c:
    print(a)
if b>c and b>a:
    print(b)

if c>a and c>b:
    print(c)"""
#2) Excercise

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if a>=b:
    if a>=c:
        print(a)
    else:
        print(c)
else:
    if b>=c:
        print(b)
    else:
        print(c)

