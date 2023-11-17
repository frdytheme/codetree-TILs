A, B = input(), input()
a, b = "", ""
for c in A:
    if "0" <= c <= "9":
        a += c

for c in B:
    if "0" <= c <= "9":
        b += c

print(int(a) + int(b))