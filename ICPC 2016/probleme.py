import math

def main(val):
    a, b = finda_and_b(val)
    print("{}^{}".format(int(a), b))

def finda_and_b(n):
    max = int(math.sqrt(n))
    if isprime(n):
        return n, 1
    for b in reversed(range(2, max)):
        a = (n**(1/float(b)))
        if int(a) == a:
            return a, b

def isprime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    vals = []
    while True:
        inputs = input().strip()
        if inputs == '-1':
            break
        else:
            vals.append(int(inputs))
    for val in vals:
        main(val)