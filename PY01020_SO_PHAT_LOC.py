t = int(input())
for _ in range(t):
    s = input()
    if s[len(s) - 2:] == "86":
        print("YES")
    else:
        print("NO")
