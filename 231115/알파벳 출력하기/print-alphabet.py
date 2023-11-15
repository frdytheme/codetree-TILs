n = int(input())
cnt = 65

for i in range(n):
    for _ in range(i+1):
        print(chr(cnt),end="")
        if chr(cnt) == "Z":
            cnt = 65
        else:
            cnt += 1
    print()