arr = input().split()
a, b = int(arr[0]), int(arr[1])

print(f"{1 if a < b else 0} {1 if a == b else 0}")