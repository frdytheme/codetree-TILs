s = input()

idx = s.index("e")
s = s[:idx] + s[idx + 1:]
print(s)