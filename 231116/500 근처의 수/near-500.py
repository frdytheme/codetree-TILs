nums = list(map(int, input().split()))
under_max = 1
over_min = 1000
for n in nums:
    if n < 500 and under_max < n:
        under_max = n
    if n > 500 and over_min > n:
        over_min = n

print(under_max, over_min)