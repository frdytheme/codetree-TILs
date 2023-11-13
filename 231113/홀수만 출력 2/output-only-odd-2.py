num = input().split()
a, b = int(num[1]), int(num[0])

for i in range(b, a-1, -2):
    print(i, end=" ")