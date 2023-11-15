n = input()
arr = list(map(int, input().split()))
evens = []
for x in arr:
    if x % 2 == 0:
        evens.append(x)
for even in evens[::-1]:
    print(even, end=" ")