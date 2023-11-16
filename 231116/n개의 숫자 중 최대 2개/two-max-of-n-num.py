N = int(input())
nums = list(map(int, input().split()))

arr = []
min_num = min(nums)
for n in range(3):
    max_num = max(nums)
    idx = nums.index(max_num)
    arr.append(max_num)
    nums[idx] = min_num
print(arr[0], arr[1])