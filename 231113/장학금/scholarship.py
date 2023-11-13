s = input().split()
middle, end = int(s[0]), int(s[1])

if middle < 90:
    print(0)
elif end >= 95:
    print(100000)
elif end >= 90:
    print(50000)
else:
    print(0)