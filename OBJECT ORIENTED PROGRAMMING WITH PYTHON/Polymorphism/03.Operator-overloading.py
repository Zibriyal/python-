class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __add__(self,other):
        return product(self.name,self.price+other.price)

p1=product('apple',10)
p2=product('banana',20)
print(p1+p2)