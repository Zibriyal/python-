def sum(*elements):
    res=0
    for x in elements:
        res += x
    return res

print(sum(10,20))

print(sum(10,20,30))

print(sum(10))

print(sum())


print("------------------------------------------------------------------------------------")



def sum(init_sum,*elements):
    res=init_sum
    for x in elements:
        res+=x
    return res
print(sum(0,10,20))
print(sum(10,20,30))

print("------------------------------------------------------------------------------------")



def printElements(*elements):
    print(elements)

printElements(101,'abc',100)
printElements(102,'xyz',200)

print("------------------------------------------------------------------------------------")

#Keyword variable length arguments

def printDetails(**details):
    for d,v in details.items():
        print(f"{d} is {v}")

printDetails(id=101,name='abc',price=100)
print()
printDetails(id=102,name='xyz')


print("------------------------------------------------------------------------------------")



def printDetails(id,**details):
    print(f"Details of {id}:")
    for d,v in details.items():
        print(f"{d} is {v}")

printDetails(101,name='abc',price=100)
print()
printDetails(102,name='xyz',color='black' )