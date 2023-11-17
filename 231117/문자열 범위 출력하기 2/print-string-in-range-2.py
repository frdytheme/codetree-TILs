s, n = input(), int(input())

for i in range(len(s) - 1, -1, -1):
    if i < len(s) - n:
        break
    print(s[i], end="")