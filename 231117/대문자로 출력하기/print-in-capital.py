s = input()

for c in s:
    if "A" <= c <= "z":
        if "a" <= c <= "z":
            print(c.upper(), end="")
        else:
            print(c, end="")