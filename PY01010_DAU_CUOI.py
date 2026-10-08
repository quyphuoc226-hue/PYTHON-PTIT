t = int(input())
for _ in range(t):
    s = input()
    if s[:2] == s[len(s) - 2:]:
        print("YES")
    else:
        print("NO")