arr = list(map(int, input().split()))
stack = []
for n in arr:
    if n == 0:
        break
    stack.append(n)
print(sum(stack), format(sum(stack) / len(stack), ".1f"))