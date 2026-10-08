t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(22, n):
        s = str(i)
        if s == s[::-1] and len(s) % 2 == 0 and all(c in "02468" for c in s):
            print(s, end = " ")
    print(end = "\n")