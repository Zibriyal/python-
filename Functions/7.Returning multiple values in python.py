def add_multily(x,y):
    sum = x + y
    mul = x * y
    return sum, mul

s,m = add_multily(10,30)
print(s)
print(m)


#To return list

def add_mul_sub(x,y):
    sum = x + y
    mul = x * y
    sub = x - y
    return [sum, mul, sub]

s,m,sb=add_mul_sub(10,30)
print(s)
print(m)
print(sb)

#Return dictionary

def add_mul_sub(x,y):
    return {
        'sum': x + y,
        'mul': x * y,
        'sub': x - y
    }

result=add_mul_sub(10,30)
print('sum is',result['sum'])
print('mul is',result['mul'])
print('sub is',result['sub'])