n = int(input())
nums = list(map(int, input().split()))

buy = nums[0]
val = []
for i in nums[1:]:
    if buy < i:
        val.append(i - buy)
    else:
        buy = i
if len(val) > 0:
    print(max(val))
else:
    print(0)