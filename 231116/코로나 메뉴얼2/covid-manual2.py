arr = [0] * 4
for _ in range(3):
    a, b = tuple(map(str, input().split()))
    b = int(b)
    if a == "Y":
        if b >= 37:
            arr[0] += 1
        else:
            arr[2] += 1
    else:
        if b >= 37:
            arr[1] += 1
        else:
            arr[3] += 1
if arr[0] >= 2:
    arr.append("E")
for i in arr:
    print(i,end=" ")