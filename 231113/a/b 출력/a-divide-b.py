num = input().split()
a, b = int(num[0]), int(num[1])
print(f"{a//b}.", end="")
a %= b
for _ in range(20):
    a *= 10
    print(a // b, end="")
    a %= b