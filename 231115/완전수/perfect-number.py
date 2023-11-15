arr = input().split()
s, e = int(arr[0]), int(arr[1])
cnt = 0
for i in range(s, e+1):
    val = 1
    for d in range(2, i):
        if i % d == 0:
            val += d
    if val == i:
        cnt += 1
print(cnt)