arr = input().split()
a, b = int(arr[0]), int(arr[1])

for i in range(a):
    for j in range(b):
        print((j+1)*(i+1), end=" ")
    print()