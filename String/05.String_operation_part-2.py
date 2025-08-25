s1=('geeks')
print(len(s1))

s2=s1.upper()
print(s2)
s3=s2.lower()
print(s3)
print(s1.islower())
print(s2.isupper())

print("--------------------------------------------------------")
#startswith &  endswith method
s="GeeksforGeeks python course"
print(s.startswith('Geeks'))
print(s.endswith('course'))
print(s.startswith('Geeks',1))
print(s.startswith('Geeks',8,len(s)))

print("--------------------------------------------------------")


#split and join method

s1='geeksforgeeks'
print(s1.split( ))

s2='geeks,for,geeks'
print(s2.split(','))

l=['geeksforgeeks','python','course']
print(' '.join(l))
print(','.join(l))

print("--------------------------------------------------------")

#strip method-to remove unwanted charaters from string

s='--geeksforgeeks---'

print(s.strip('-'))
print(s.lstrip('-'))
print(s.rstrip('-'))
print(s.rstrip('-'))

print("--------------------------------------------------------")


#find method

s1='geeksforgeeks'
s2='geeks'

print(s1.find(s2))
print(s1.find('gfg'))
n=len(s1)
print(s1.find(s2   ,1,n))
