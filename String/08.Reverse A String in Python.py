s=input('Enter a string: ')
rev=" "
for i in s:
    rev=i+rev
print(rev)


#Method 2: Shortcut Method Using String Slicing


print(s[::-1])