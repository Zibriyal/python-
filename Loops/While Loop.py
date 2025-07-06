#The programme to print text 5 times
i=10                                        # counter
while i<5:
    print("Geeksfor geeks")
    i=i+1



"""
Infinite loop as value of 'i' is constant '0',so loop remains true and keep printing text infinite times

i=0                                        
while i<5:
    print("Geeksfor geeks")
    
    OR
while True:
    print("Geeksfor geeks")
"""


"""
Empty output as condition is already false

i=10                                        
while i<5:
    print("Geeksfor geeks")
"""

n=int(input("Enter a number: "))

i=0
while i<n:
    print("Geeksfor geeks")
    i=i+1