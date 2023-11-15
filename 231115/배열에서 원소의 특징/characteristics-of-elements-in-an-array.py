arr = list(map(int, input().split()))
val = 0
for n in arr[1:]:
    if n % 3 == 0:
        break
    val = n
print(val)