
"""a=int(input("Enter a:"))
b=int(input("Enter b:"))
res=max(a,b)
while res<= a*b:
    if res%a==0 and res%b==0:
        break
    res=res+1
print("The LCM is :",res)
"""

import math
a=int(input("Enter a:"))
b=int(input("Enter b:"))
res=math.gcd(a,b)
lcm=(a*b)//res
print("The LCM is :",lcm)