s = input()
thuong = 0
for c in s:
    if c.islower():
        thuong += 1
if thuong >= len(s) - thuong:
    s = s.lower()
else:
    s = s.upper()
print(s)
