#To break the loop as soon as condition is met

#Find the smallest division of a number such that the divisor is greater than 1:

"""n=int(input("Enter n:"))
for x in range(2,n+1):                             # 2 , divisor is greater than 1
    if n%x==0:

        print(x)
        break
"""
#USing while Lopp
"""n=int(input("enter n:"))

x=2
while x<=n:
    if n%x==0:
        print(x)
        break
    x=x+1  """

i=1
while i<=5:
    if i==3:
        break
    print(i)
    i=i+1
print(i)

