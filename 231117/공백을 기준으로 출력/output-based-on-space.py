a, b = input(), input()
s = a + b
for i in range(len(a)+len(b)):
    if s[i] != " ":
        print(s[i],end="")