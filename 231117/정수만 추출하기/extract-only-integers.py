A, B = tuple(input().split())

a, b = "", ""
for c in A:
    if "0" <= c <= "9":
        a += c
    else:
        break

for c in B:
    if "0" <= c <= "9":
        b += c
    else:
        break

print(int(a) + int(b))