t = int(input())
for _ in range(t):
    n = int(input())
    mu = 10
    while n > mu:
        if n % mu >= mu // 2:
            n = (n // mu + 1) * mu
        else:
            n = (n // mu) * mu
        mu *= 10
    print(n, end = "\n")