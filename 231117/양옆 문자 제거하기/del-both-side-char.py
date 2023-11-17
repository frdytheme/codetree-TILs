s = input()
r = s[:2] + s[3:-2] + s[-1] #success

s = list(s)
s.pop(2), s.pop(-2)
r = "".join(s)

print(r)