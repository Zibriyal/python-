# 1) using %
name="ABC"
course="Python course"
s="Welcome %s to the %s "%(name,course)
print(s)

#2) using format() function

s="Welcome {0} to the {1}".format(name,course)
print(s)

#3) using f-string
s=f"Welcome {name} to the {course}"
print(s)


a=10
b=20
print(f"sum of {a} and {b} is {a+b}")
print(f"product of {a} and {b} is {a*b}")


s1="ABC"
s2="abc"
print(f"Lowercase of {s1} is {s1.lower()}")
print(f"uppercase of {s2} is {s2.upper()}")
