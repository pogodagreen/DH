import random


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def GCD(x, y):
    while y != 0:
        pom = y
        y = x % y
        x = pom
    return x


def isCoPrime(x, y):
    if GCD(x, y) == 1:
        return True
    return False

def primRoots(modulo):
    

if __name__ == '__main__':
    n = random.randrange(1000, 10000)
    while not isPrime(n):
        n = random.randrange(1000, 10000)
    print ("n", n)
