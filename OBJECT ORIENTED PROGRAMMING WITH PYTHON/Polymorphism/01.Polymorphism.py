"""Polymorphism is one of the four fundamental features in object-oriented programming (OOP). The other three features are encapsulation, inheritance, and abstraction. Polymorphism allows a single name to have different forms.

Types of Polymorphism
Polymorphism is categorized into two types:

Static Polymorphism: Also known as compile-time polymorphism.
Dynamic Polymorphism: Also known as runtime polymorphism."""

"""
Static Polymorphism
In languages like C++ and Java, static polymorphism is typically achieved through function overloading.
Function overloading allows multiple functions to have the same name but different parameters.
"""

"""Dynamic Polymorphism in Python
Despite the limitation with static polymorphism, Python inherently supports dynamic polymorphism. This is because Python is a dynamically typed language, meaning you don't need to specify data types explicitly.
A single function can accept different types of data"""

def fun(a, b):
    print(a)
    print(b)

def fun(a, b, c):
    print(a)
    print(b)
    print(c)

def fun(l):
    for x in l:
        print(x)

#fun(10, 20)  # This will result in an error due to multiple definitions of fun() with different number of arguments

fun([10, 20])  # Output: 10 20