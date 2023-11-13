num = input().split()
a, b = int(num[0]), int(num[1])

if a > b:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
else:
    while b >= a:
        print(b, end=" ")
        b -= 1