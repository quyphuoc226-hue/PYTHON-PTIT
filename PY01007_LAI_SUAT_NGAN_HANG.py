t = int(input())
for _ in range(t):
    n, x, m = map(float, input().split())
    nam = 0
    while n < m:
        n += n * x // 100
        nam += 1
    print(nam)