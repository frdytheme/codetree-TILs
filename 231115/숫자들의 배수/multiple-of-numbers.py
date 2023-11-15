n = int(input())
stack = [n]
cnt = 0
for i in stack:
    print(stack[-1], end=" ")
    stack.append(n * (len(stack) + 1))
    if stack[-1] % 5 == 0:
        cnt += 1
    if cnt >= 2:
        print(stack[-1], end=" ")
        break