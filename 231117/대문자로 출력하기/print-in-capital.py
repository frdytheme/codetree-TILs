s = input()

for c in s:
    if "a" <= c <= "z":
        print(c.upper(), end="")
    if "A" <= c <= "Z":
        print(c, end="")