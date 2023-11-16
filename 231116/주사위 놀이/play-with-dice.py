dice = list(map(int, input().split()))
board = [0] * 6

for n in dice:
    board[n-1] += 1
for i in range(1, 7):
    print(f"{i} - {board[i-1]}")