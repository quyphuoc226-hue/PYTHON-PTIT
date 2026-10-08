t = int(input())
for _ in range(t):
    n = input()
    tong = 0
    for c in n:
        tong += int(c)
    if tong != int(str(tong)[::-1]) or tong < 10:
        print("NO")
    else:
        print("YES")