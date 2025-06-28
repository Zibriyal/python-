#Even ODd  "If else"
"""
n=int(input('Enter n:'))
if n%2==0:
    print("even")

else:
    print("odd")
"""

#Positive , negative or Zero "If else elif"
"""
n=int(input('Enter n:'))
if n>0:
    print("positive")

elif n<0:
    print("negative")

else:
    print("zero")
"""

#Decide if an input number is "Nested if else"
"""
n=int(input('Enter n:'))
if n>0:
    print("positive",end=" ")
    if n%2==0:
        print("even")
    else:
        print("odd")

elif n<0:
    print("negative",end=" ")
    if n%2==0:
        print("even")
    else:
        print("odd")

else:
    print("zero")
"""

#Excercise

"""a=int(input('Enter a:'))
b=int(input('Enter b:'))

if a>b:
    print("a is greater")
elif b>a:
    print("b is greater")
else:
    print("a and b are same")"""

n=int(input('Enter n:'))
print("The winner is :")

if n%2==0:
    print("Opponent")

else:
    print("You")

