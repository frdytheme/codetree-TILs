nums = list(map(int, input().split()))
min_num = nums[0]
for n in nums[1:]:
    if n > min_num:
        min_num = n
print(min_num)