from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = input()
    tong = 0
    for c in n:
        tong += int(c)
    if prime(tong):
        print("YES")
    else:
        print("NO")