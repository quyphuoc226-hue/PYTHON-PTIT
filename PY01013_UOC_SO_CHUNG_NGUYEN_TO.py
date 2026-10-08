from math import sqrt

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s = str(gcd(a, b))
    tong = 0
    for c in s:
        tong += int(c)
    if prime(tong):
        print("YES")
    else:
        print("NO")
