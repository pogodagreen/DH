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
    roots = []
    required_set = set(num for num in range (1, modulo) if GCD(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)
    return roots


if __name__ == '__main__':
    n = random.randrange(10, 100)
    while not isPrime(n):
        n = random.randrange(10, 100)
    print ("n", n)
    print(primRoots(n))
    g=max(primRoots(n))
    print(g)

    #A
    x = random.randrange(10, 100)
    while not isPrime(n):
        x = random.randrange(10, 100)
    X=g**x %n

    #B
    y = random.randrange(10, 100)
    while not isPrime(n):
        y = random.randrange(10, 100)
    Y = g ** y % n

    #A
    k1=Y**x %n
    print(k1)

    #B
    k2=X**y %n
    print(k2)

    if(k1==k2):
        print("It's the same")
    else:
        print ("They're not the same")