arr = list(map(int, input().split()))
odd = 0
even = 0
for i in range(len(arr)):
    if i % 2 != 0:
        even += arr[i]
    else:
        odd += arr[i]
if odd > even:
    print(odd - even)
else:
    print(even - odd)