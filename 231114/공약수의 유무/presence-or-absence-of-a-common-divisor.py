arr = input().split()
a, b = int(arr[0]), int(arr[1])

for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        print(1)
        break
    else:
        print(0)