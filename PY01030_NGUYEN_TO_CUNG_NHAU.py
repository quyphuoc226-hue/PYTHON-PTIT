from math import pow


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

n, k = map(int, input().split())
st = 1
en = 1
for i in range(0, k - 1):
    st = st * 10
for i in range(0, k):
    en = en * 10
en -= 1
dem = 0
for i in range(st, en):
    if dem == 10:
        print()
        dem = 0
    if gcd(n, i) == 1:
        print(i, end = " ")
        dem += 1