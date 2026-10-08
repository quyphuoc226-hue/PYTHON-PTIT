from math import sqrt

a = [1] * 10005
def sang():
    a[0] = a[1] = 0
    for i in range (2, int(sqrt(10005)) + 1):
        if a[i] == 1:
            for j in range(i * i, 10005, i):
                a[j] = 0

sang()
t = int(input())
for _ in range(t):
    n = input()
    n = int(n[len(n) - 4:])
    if a[n] == 1:
        print("YES")
    else:
        print("NO")