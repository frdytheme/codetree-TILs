N = int(input())
nums = list(map(int, input().split()))
arr = []

while True:
    if len(nums) == 0:
        break
    max_num = max(nums)
    idx = nums.index(max_num)
    arr.append(idx + 1)
    nums = nums[:idx]

for i in arr:
    print(i, end=" ")