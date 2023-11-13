num = input().split()
a, b = int(num[0]), int(num[1])

while a <= b:
    print(a, end=" ")
    if a % 2 == 0:
        a += 3
    else:
        a *= 2