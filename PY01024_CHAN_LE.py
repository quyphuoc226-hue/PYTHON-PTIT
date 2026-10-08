t = int(input())
for _ in range(t):
    s = input()
    ok = True
    tong = 0
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) != 2:
            ok = False
            break
        tong += int(s[i])
    tong += int(s[len(s) - 1])
    if tong % 10 != 0:
        ok = False
    if ok:
        print("YES")
    else:
        print("NO")
