"""l=[10,16,17,18,19,15]

for i in l:
    if i%5==0:
        continue
    print(i,end=' ')

"""
# Skipping the 3
# Skipping the 3
"""i=0
while i<=5:
    if i==3:
        i=i+1
        continue
    print(i,i*i)
    i=i+1
"""

l=[10,16,17,18,9,15,21,13]

for x in l:
    if x%5==0:
        continue
    if x%7==0:
        break
    print(x)
print("bye")
