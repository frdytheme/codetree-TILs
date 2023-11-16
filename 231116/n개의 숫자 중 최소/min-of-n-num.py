N = int(input())
nums = list(map(int, input().split()))
cnt = 0
min_num = min(nums)
for n in nums:
    if n == min_num:
        cnt += 1
print(min_num, cnt)