s = input()

for i in range(len(s)):
    c = s[i]
    if ord(c) >= ord("A") and ord(c) <= ord("z"):
        if ord(c) >= ord("Z"):
            # idx = ord(c) + ord("A") - ord("a")
            # print(chr(idx), end="")
            print(c.upper(), end="")
        else:
            print(c, end="")