#1) check for substring
from xml.dom.pulldom import SAX2DOM

s1="geeksforgeeks"
s2="geeks"

print(s2 in s1)
print(s2 not in s1)


#2)Concatenation

s1="geeks"
s2="forgeeks"
s3=s1+s2
s4="welcome to " +s1+s2
print(s3)
print(s4)

#3) Finding position of a substring

s1="geeksforgeeks"
s2="geeks"
print(s1.index(s2))           #Start
print(s1.rindex(s2))            #Last
print(s1.index(s2,0,13))  #start from 0 to 13

print("--------------------------------------------------------------------------")
#4) Finding Substring Position using rindex() Method

s1="geeksforgeeks"

last_geek=s1.rindex('geeks')
print(last_geek)

last_e=s1.rindex('e')
print(last_e)

last_forge=s1.rindex('forge',2)
print(last_forge)

last_ks=s1.rindex('ks',0,-2)
print(last_ks)