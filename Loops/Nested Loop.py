#print tables of number from 1 to 10.
"""
for i in range(1,1*10+1,1):
    print(i,end=" ")
print()


for i in range(2,2*10+1,2):
    print(i,end=" ")
print()

for i in range(3,3*10+1,3):
    print(i,end=" ")
print()

"""

"""for i in range(1,11):
    for j in range(i,i*10+1,i):
        print(j,end=" ")
    print()
"""

"""for i in range(1,3):
    j=1
    while j<3:
        print(i,j)
        j=j+1
    print("GFG")"""
ll=[[10,20,30],[40,50,60],[70,80]]

for i in ll:
    for x in i:
        print(x,end=" ")
    print()