a=['geeks','for','geeks']
print(a)

#Creating a List in Python

l=[]
print("Blank list:")
print(l)

# Creating a List of Numbers

l=[10,20,30]
print('List of numbers:')
print(l)

# Creating a List of Strings and Accessing Elements

l=['geeks','for','geeks']
print('List of items:')
print(l[0])
print(l[2])

#Accessing Elements from a List
l=['geeks','for','geeks']
print("Accessing Elements from a List")
print(l[0])
print(l[2])

#Accessing Elements from a Multi-Dimensional List

l=[['geeks','for'],['geeks']]
print('Accessing Elements from a Multi-Dimensional List')
print(l[0][1])
print(l[1][0])


#Negative Indexing

l=[1,2,'geeks',4,'for',6,'geeks']
print('Accessing elements using negative indexing')
print(l[-1])
print(l[-3])


#Getting the Size of the Python List

l1=[]
print(len(l1))

l2=[10,20,14]
print(len(l2))

#Adding Elements to a Python List
# append() method

l=[]
print('Initial blank list')
print(l)

l.append(1)
l.append(2)
l.append(4)
print('\nList after addition of three elements')
print(l)

for i in range(1,4):
    l.append(i)
print('\nList after addition of elemets from 1-3:')
print(l)

l.append((5,6))
print('\nList after addition of Tuple:')
print(l)

l2=['for','geeks']
l.append(l2)
print('\nList after addition of lists:')
print(l)

#Using insert() method:

l=['geeks','geeks']
l.insert(1,'for')
print(l)

l1=[1,2,3,4,5,6,7]
l1.insert(4,10)
print(l1)

#count() method
l2=['a','a','a','b','b','a','c','b']
print(l2.count('b'))

#del Keyword
"""del list_name[index]  &#35; To delete a single item
del list_name        &#35; To delete the entire list"""

num=[1,2,3,2,3,4,5]
del num[2]
print(num)

del num[-1]
print(num)

del num[0]
print(num)

#remove() method
#The remove() method removes the first occurrence of a specified value from the list.

"""list_name.remove(value)"""

num=[1,2,3,2,3,4,5]
num.remove(3)
print(num)

num.remove(2)
print(num)

num.remove(5)
print(num)

#pop() method
#removes and returns an item at a specified index
#If no index is specified, it removes and returns the last item.

"""list_name.pop(index)"""
num=[1,2,3,2,3,4,5]
num.pop(3)
print(num)

num.pop(-1)
print(num)

num.pop(0)
print(num)

#max() method
#function returns the largest value among the provided argument
#If strings are provided, it returns the lexicographically largest string.

"""max(a, b, c, ..., key=None, default=None)"""

print("maximum of 4,12,43.3,19 and 100 is :",end="")
print(max(4,12,43.3,19,100))

#min() method
print("minimum of 4,12,43.3,19 and 100 is :",end="")
print(min(4,12,43.3,19,100))

#sort() function
#The sort() function sorts a list in ascending, descending, or a user-defined order.

"""List_name.sort(reverse=True/False, key=None)"""

num=[1,3,4,2]
num.sort()
print(num)

#reverse() method
#The reverse() method reverses the elements of the list in place without using extra space

l=[1,2,3,4,1,2,6]
l.reverse()
print(l)

l1=['a','b','c','d','a','a']
l1.reverse()
print(l1)