def check(n):
    if n != n[::-1]:
        return False
    if len(n) % 2 != 0:
        return False
    for c in n:
        if int(c) % 2 != 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(22, n, 11):
        if check(str(i)):
            print(i, end = " ")
    print()
