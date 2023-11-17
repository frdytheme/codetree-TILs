a, b = tuple(input().split())

c = ord(a) + ord(b)
d = 0
if ord(a) > ord(b):
    d = ord(a) - ord(b)
else:
    d = ord(b) - ord(a)
print(c, d)