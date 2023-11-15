arr = list(map(int, input().split()))
even = arr[1::2]
third = arr[2::3]
avg = round(sum(third) / len(third), 1)
print(sum(even),avg)