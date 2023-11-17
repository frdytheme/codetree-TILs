a, b = tuple(map(int, input().split()))

n = a + b
cnt = 0

for c in str(n):
    if c == "1":
        cnt += 1

print(cnt)