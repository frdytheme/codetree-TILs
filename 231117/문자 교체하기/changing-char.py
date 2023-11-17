a, b = tuple(input().split())

b = list(b)

b[0] = a[0]
b[1] = a[1]

print("".join(b))