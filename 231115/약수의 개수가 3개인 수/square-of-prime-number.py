arr = input().split()
s, e = int(arr[0]), int(arr[1])
val = 0
for i in range(s, e+1):
    cnt = 1
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 3:
        val += 1
print(val)