n = int(input())

arr = [
    [0 for _ in range(i+1)]
    for i in range(n)
]

num = 1
for row in range(n):
    for col in range(row+1):
        if row == 0 or col == 0 or col == row:
            arr[row][col] = 1
        else:
            arr[row][col] = arr[row-1][col-1] + arr[row-1][col]

for row in arr:
    for col in row:
        print(col,end=" ")
    print()