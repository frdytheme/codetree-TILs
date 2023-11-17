s = input()

for c in s:
    if "a" <= c <= "z":
        print(c.upper(), end="")
    else:
        print(c.lower(), end="")