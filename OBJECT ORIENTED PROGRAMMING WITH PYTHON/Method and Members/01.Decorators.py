"""unctions in Python have some unique properties that are essential to understand decorators. The first property is that functions are first-class objects. In Python, everything is an object. Whether you create an integer, a string, or any other type of variable, it is an object of a class. Similarly, functions are also objects, which means they can be treated like any other variable.

You can assign a function to a variable and call the function using that variable name. Not only that, you can assign functions to multiple variables, pass them as arguments to other functions, return them from functions, and store them in data structures like dictionaries. This flexibility is a powerful feature of Python functions.

Inner Functions
The second property is that a function can have inner functions. This means you can define functions inside other functions. These inner functions are locally scoped to the enclosing function and can only be used within that function. This allows for better organization of code and encapsulation of functionality.

Understanding Decorators
A decorator is a function that takes another function as an argument and enhances the behavior of the passed function. Decorators leverage the two properties of functions mentioned earlier: first-class objects and inner functions. By using decorators, you can modify or extend the behavior of functions without changing their actual code."""
#Bsic decorator example


def fun1():
    print("Inside fun1")

def fun2(f):
    print("Inside fun2")
    f()

f=fun1
f()
print()
fun2(f)


print("--------------------------------------------------")
"""Function inside a function"""

def fun2():
    print("Inside fun2")
    def fun1():
        print("Inside fun1")
    fun1()

fun2()

print("-------------------An example decorator-------------------------------")

def decfun(f):
    def innerfun():
        print("Welcome")
        f()
    return innerfun
def fun():
    print("User")
fun=decfun(fun)
fun()

print("------------------------Short cut method--------------------------")

def decfun(f):
    def innerfun():
        print("Welcome")
        f()
    return innerfun
@decfun
def fun():
    print("User")

fun()