s = list(input())

a, b = s[0], s[1]

for i in range(1, len(s)):
    if s[i] == b:
        s[i] = a
print("".join(s))