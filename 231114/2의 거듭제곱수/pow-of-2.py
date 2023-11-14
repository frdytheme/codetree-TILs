n = int(input())
x = 1
while True:
    if n // 2 == 1:
        break
    x += 1
    n = n // 2
print(x)