n = int(input())
cnt = 1
for i in range(n):
    for _ in range(cnt):
        print("*", end="")
    cnt += 2
    print()