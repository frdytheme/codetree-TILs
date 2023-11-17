s, q = tuple(input().split())

for _ in range(int(q)):
    t = int(input())
    if t == 1:
        s = s[1:] + s[0]
    if t == 2:
        s = s[-1] + s[:-1]
    if t == 3:
        s = s[::-1]
    print(s)