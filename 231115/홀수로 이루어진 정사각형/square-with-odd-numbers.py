n = int(input())

for i in range(n):
    for j in range(1, n + 1):
        print((j * 2) + (i * 2 + 9),end=" ")
    print()