arr = list(map(int, input().split()))
stack = []
val = 0
for num in arr:
    if num >= 250:
        break
    stack.append(num)
    val += num
print(val, format(val / len(stack), ".1f"))