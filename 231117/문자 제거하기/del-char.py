s = list(input())

while len(s) > 1:
    d = int(input())
    if d >= len(s):
        s = s[:-1]
    else:
        s.pop(d)
    print("".join(s))