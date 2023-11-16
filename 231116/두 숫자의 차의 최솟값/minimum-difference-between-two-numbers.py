n = int(input())
nums = list(map(int, input().split()))
min_val = 100
for i in range(n-1):
    val = nums[i+1] - nums[i]
    if val < min_val:
        min_val = val
print(min_val)