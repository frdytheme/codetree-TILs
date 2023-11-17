s = input()

for c in s:
    if "a" <= c <= "z" or "A" <= c <= "Z" or "0" <= c <= "9":
        print(c.lower(), end="")