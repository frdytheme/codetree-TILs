a, b = tuple(map(int, input().split()))
arr = [0] * 10
while a > 1:
    arr[a % b] += 1
    a = a // b
val = 0
for i in arr:
    n = i ** 2
    val += n
print(val)