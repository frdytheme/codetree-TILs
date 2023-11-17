s, q = tuple(input().split())
s = list(s)
for _ in range(int(q)):
    t, a, b = tuple(input().split())
    if int(t) == 1:
        a, b = int(a)-1, int(b)-1
        s[a], s[b] = s[b], s[a]
    elif int(t) == 2:
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
    print("".join(s))