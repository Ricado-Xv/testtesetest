from functools import reduce
def prod(x,y):
    return x*y
s=reduce(prod, [3,5,7,9])
print(s)
