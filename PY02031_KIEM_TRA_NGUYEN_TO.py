from math import sqrt

prime = [1] * 1005
def sang():
    prime[0] = prime[1] = 0
    for i in range(2, int(sqrt(1005)) + 1):
        if prime[i] == 1:
            for j in range(i * i, 1005, i):
                prime[j] = 0

sang()
n, m = map(int, input().split())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
for i in range(n):
    for j in range(m):
        if prime[a[i][j]]:
            print("1", end = " ")
        else:
            print("0", end = " ")
    print()