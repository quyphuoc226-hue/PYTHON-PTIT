t = int(input())
for _ in range(t):
    n = input()
    ok = True
    for c in n:
        if c != '4' and c != '7':
            ok = False
    if ok:
        print("YES")
    else:
        print("NO")