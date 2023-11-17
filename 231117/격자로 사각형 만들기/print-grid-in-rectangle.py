n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for row in range(n):
    for col in range(n):
        arr[0][col] = 1
        arr[row][0] = 1
for row in range(1, n):
    for col in range(1, n):
        arr[row][col] = arr[row-1][col] + arr[row-1][col-1] + arr[row][col-1]

for row in arr:
    for col in row:
        print(col,end=" ")
    print()