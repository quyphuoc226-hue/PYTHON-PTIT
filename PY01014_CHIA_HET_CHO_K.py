a, k, n = map(int, input().split())
if n - a <= 0:
    print(-1)
else:
    first = k - a % k
    if first > n - a:
        print(-1)
    else:
        for i in range(first, n - a + 1, k):
            print(i, end = " ")
