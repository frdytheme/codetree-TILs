n = int(input())
nums = list(map(int, input().split()))

for _ in range(2):
    nums[nums.index(2)] = 0
print(nums.index(2) + 1)