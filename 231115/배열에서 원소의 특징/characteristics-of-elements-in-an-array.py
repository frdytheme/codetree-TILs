arr = list(map(int, input().split()))
stack = []
for n in arr:
    if n % 3 == 0 and n >= 3:
        break
    stack.append(n)
print(stack[-1])