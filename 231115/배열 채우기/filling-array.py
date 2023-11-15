arr = list(map(int, input().split()))
stack = []
for n in arr:
    if n == 0:
        break
    stack.append(n)
for c in stack[::-1]:
    print(c,end=" ")