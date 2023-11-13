arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

print(f"{int(a <= b and a <= c)} {int(a == b and b == c)}")