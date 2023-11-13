num = input().split()
a, b = int(num[1]), int(num[0])

while b >= a:
    print(b, end=" ")
    b -= 2