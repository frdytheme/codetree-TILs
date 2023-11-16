arr = list(map(int, input().split()))
board = [0] * 10

for s in arr:
    if s == 0:
        break
    n = s // 10
    board[n-1] += 1
for i in range(10,0,-1):
    print(f"{i*10} - {board[i-1]}")