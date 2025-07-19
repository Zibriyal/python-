"""def getfirstdigit(X):
    while X>=10:
        X=X//10
    return X

X=int(input('enter the number'))
print(getfirstdigit(X))

"""

import math
def getfirstdigit(X):
    d=int(math.log10(X))
    res=X//(10**d)
    return res
X=int(input('enter the number'))
print(getfirstdigit(X))


