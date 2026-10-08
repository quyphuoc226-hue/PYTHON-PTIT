from math import sqrt
mx = 10005
a = [0] * mx
def sang():
    for i in range(mx):
        a[i] = 1
    a[0] = 0
    a[1] = 0
    for i in range(2, int(sqrt(mx)) + 1):
        if a[i] == 1:
            for j in range(i * i, mx, i):
                a[j] = 0
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
sang()
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            cnt += 1
    if a[cnt] == 1:
        print("YES")
    else:
        print("NO")