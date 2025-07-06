#To count the digits in a number

x=int(input("enter x :"))

res=0

while x >0:

    x=x//10

    res=res+1

print("The count of digit is",res)