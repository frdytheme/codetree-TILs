n, m = map(int,input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
num = 1


for col in range(m):
    now_row = 0
    now_col = col

    while 0 <= now_col and now_row < n:
        arr[now_row][now_col] = num
        now_row += 1
        now_col -= 1
        num += 1

for row in range(1, n):
    now_row = row
    now_col = m - 1
    
    while 0 <= now_col and now_row < n:
        arr[now_row][now_col] = num
        now_row += 1
        now_col -= 1
        num += 1

for row in arr:
    for col in row:
        print(col,end=" ")
    print()