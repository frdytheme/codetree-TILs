nums = list(map(int, input().split()))
arr = []

for n in nums:
    if n == 999 or n == -999:
        break
    arr.append(n)

min_num = arr[0]
max_num = arr[0]

for n in arr[1:]:
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n

print(max_num, min_num)