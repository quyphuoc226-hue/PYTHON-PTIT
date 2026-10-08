from math import sqrt

a = [1] * 505
def sang():
    a[0] = a[1] = 0
    for i in range(2, int(sqrt(505)) + 1):
        if a[i] == 1:
            for j in range(i * i, 505, i):
                a[j] = 0
sang()
t = int(input())
for _ in range(t):
    n = input()
    cnt = 0
    for c in n:
        if c == '2' or c == '3' or c == '5' or c == '7':
            cnt += 1
    if a[len(n)] == 1 and cnt > len(n) - cnt:
        print("YES")
    else:
        print("NO")