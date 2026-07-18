from math import sqrt

def prime(n, i):
    if i == 1:
        return True
    if n % i == 0:
        return False
    return prime(n, i - 1)

n = 13
print(prime(n, int(sqrt(n))))
