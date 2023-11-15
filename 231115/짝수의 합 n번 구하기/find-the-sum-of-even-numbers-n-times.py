n = int(input())

for i in range(n):
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])
    val = 0
    for j in range(a, b+1):
        if j % 2 == 0:
            val += j
    print(val)