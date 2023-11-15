n = int(input())
cnt = 'A'
for i in range(n):
    for _ in range(i):
        print(" ",end=" ")
    for _ in range(n, i, -1):
        print(chr(ord(cnt)),end=" ")
        if ord(cnt) == ord("Z"):
            cnt = 'A'
        else:
            cnt = chr(ord(cnt) + 1)
    print()