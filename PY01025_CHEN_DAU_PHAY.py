s = input()
ans = ""
dem = 0
for i in range(len(s) - 1, -1, -1):
    if dem == 3:
        ans += ","
        dem = 0
    ans += s[i]
    dem += 1
print(ans[::-1])