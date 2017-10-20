from fractions import gcd
from functools import reduce

def main(a, b):
    maxU, minU = a, a - b
    A = [i for i in range(minU, maxU+1)]
    return lcm(A)

def lcm(*numbers):
    def lcm(x, y):
        return x * y / gcd(x,y)
    return reduce(lcm, *numbers, 1)

if __name__ == "__main__":
    inputs = []
    while True:
        if input().split() == '-1':
            break
        val1, val2 = input().split(' ')
        inputs.append((int(val1), int(val2)))
    for vals in inputs:
        main(vals)