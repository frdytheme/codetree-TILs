arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
check = False

for i in range(a, b+1):
    if i % c == 0:
        check = True
if check:
    print("YES")
else:
    print("NO")