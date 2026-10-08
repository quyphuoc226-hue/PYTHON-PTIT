def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
t = int(input())
for _ in range(t):
    n = input()
    m = int(n[::-1])
    if gcd(int(n), m) == 1:
        print("YES")
    else:
        print("NO")