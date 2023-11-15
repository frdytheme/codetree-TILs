arr = list(map(int, input().split()))
stack = []

for i in arr:
    if i == 0:
        break
    stack.append(i)

for n in stack:
    if n % 2 == 0:
        n = n // 2
    else:
        n += 3
    print(n,end=" ")