num = input().split()
a, b = int(num[0]), int(num[1])
c = f"{a / b}"

for _ in range(19):
    c += '0'

print(c)