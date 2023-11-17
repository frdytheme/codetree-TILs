s = input()
a, b = 0, 0

for i in range(len(s) - 1):
    c = s[i:i+2]
    if c == "ee":
        a += 1
    if c == "eb":
        b += 1
print(a,b)