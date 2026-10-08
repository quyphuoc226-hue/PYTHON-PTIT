def giaithua(n):
    tich = 1
    for i in range(1, n + 1):
        tich = tich * i
    return tich
t = int(input())
for _ in range(t):
    n = input()
    tong = 0
    for c in n:
        tong += giaithua(int(c))
    if tong == int(n):
        print("Yes")
    else:
        print("No")
