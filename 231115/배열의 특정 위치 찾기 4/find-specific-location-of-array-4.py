arr = list(map(int, input().split()))
stack = []
for n in arr:
    if n == 0:
        break
    if n % 2 == 0 and n >= 2:
        stack.append(n)
print(len(stack),sum(stack))