n, m = map(int, input().split())

arr1 = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

board = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        board[i][j] = int(arr1[i][j] != arr2[i][j])

for row in board:
    for elem in row:
        print(elem,end=" ")
    print()