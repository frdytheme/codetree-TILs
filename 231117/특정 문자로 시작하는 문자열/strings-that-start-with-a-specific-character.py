n = int(input())
arr = [input() for _ in range(n)]
s = input()
cnt = 0
length = 0

for elem in arr:
    if elem[0] == s:
        cnt += 1
        length += len(elem)

print(cnt, format(length / cnt, ".2f"))