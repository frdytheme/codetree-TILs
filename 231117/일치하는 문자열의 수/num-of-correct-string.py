n, A = tuple(input().split())

cnt = 0

for i in range(int(n)):
    s = input()
    if s == A:
        cnt += 1
print(cnt)