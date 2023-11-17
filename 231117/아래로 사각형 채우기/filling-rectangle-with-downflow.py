n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 0
for i in range(n):
    for j in range(n):
        if j == 0:
            num = i + 1
        else:
            num += n
        arr[i][j] = num

for row in arr:
    for col in row:
        print(col,end=" ")
    print()