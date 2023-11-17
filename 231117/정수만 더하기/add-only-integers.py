A = input()
val = 0
for n in A:
    if "0" <= n <= "9":
        val += int(n)
print(val)