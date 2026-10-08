from math import sqrt

t = int(input())
for _ in range(t):
    n = int(input())
    print("1 *", end = " ")
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            dem = 0
            while n % i == 0:
                n = n // i
                dem += 1
            print(i, dem, sep = "^", end = " ")
            if n != 1:
                print("*", end=" ")
    if n != 1:
        print(n, "^1", sep = "", end = "")
    print()