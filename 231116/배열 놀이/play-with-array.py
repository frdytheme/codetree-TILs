n, q = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

for _ in range(q):
    qu = list(map(int, input().split()))
    if qu[0] == 1:
        print(nums[qu[1] - 1])
    if qu[0] == 2:
        if qu[1] in nums:
            print(nums.index(qu[1]) + 1)
        else:
            print(0)
    if qu[0] == 3:
        for i in range(qu[1], qu[2] + 1):
            print(nums[i -1],end=" ")
        print()