n, m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    arr[r-1][c-1] = num
    num += 1

for row in arr:
    for col in row:
        print(col,end=" ")
    print()