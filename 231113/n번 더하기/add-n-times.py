num = input().split()
a, n = int(num[0]), int(num[1])

for _ in range(n):
    a += n
    print(a)