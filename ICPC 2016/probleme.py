import math
def main():
    pass

def finda(n):
    if isprime(n):
        return n, 1
    else:
        for i in range(2, math.sqrt(n)):
            pass
            
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
    main()