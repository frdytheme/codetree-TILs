a, b = tuple(map(int, input().split()))
arr = [0] * 10
while a > 1:
    a = a // b
    i = a % b
    arr[i] += 1
arr = [i ** 2 for i in arr]
print(sum(arr))