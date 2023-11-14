while True:
    arr = input().split()
    w, h, s = int(arr[0]), int(arr[1]), arr[2]

    print(w * h)

    if s == "C":
        break