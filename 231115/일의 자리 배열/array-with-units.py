a, b = tuple(map(int, input().split()))

for i in range(10):
    print(f"{a % 10}", end=" ")
    a, b = b, a + b