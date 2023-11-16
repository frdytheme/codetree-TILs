for i in range(5):
    arr = list(map(str,input().split()))
    for s in arr:
        print(chr(ord(s) - 32),end=" ")
    print()