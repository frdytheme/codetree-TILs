arr = [
    list(map(int,input().split()))
    for _ in range(2)
]

for i in range(2):
    col_sum = 0
    for j in range(4):
        col_sum += arr[i][j]
    print(format(col_sum / 4, ".1f"), end=" ")

print()

for i in range(4):
    row_sum = 0
    for j in range(2):
        row_sum += arr[j][i]
    print(format(row_sum / 2, ".1f"), end=" ")

print()

avg = format((sum(arr[0]) + sum(arr[1])) / 8, ".1f")
print(avg)