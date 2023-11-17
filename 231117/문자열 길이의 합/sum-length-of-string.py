n = int(input())
cnt = 0
length = 0
for _ in range(n):
    s = input()
    if s[0] == "a":
        cnt += 1
    length += len(s)
print(length, cnt)