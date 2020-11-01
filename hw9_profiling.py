from math import prod



def slow(N=1000000):
    total = 0
    for i in range(N):
        total*=i
        print(total)

def pythonic(N=1000000):
    total=prod(range(N))
    return total

print(slow())

