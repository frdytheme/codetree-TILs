nums = list(map(int, input().split()))
arr = [0] * 9

for n in nums:
    if n < 10:
        continue
    a = n // 10
    arr[a-1] += 1
for i in range(1, 10):
    print(f"{i} - {arr[i-1]}")