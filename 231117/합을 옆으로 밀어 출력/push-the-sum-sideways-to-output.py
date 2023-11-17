n = int(input())

cnt = 0

for i in range(n):
    i = int(input())
    cnt += i

cnt = str(cnt)

print(cnt[1:] + cnt[0])