n = int(input())
stack = [n]
cnt = 0

for i in range(1, 10):
    stack.append(stack[-1] + 4)

for num in stack:
    print(num,end=" ")
    if num % 5 == 0:
        cnt += 1
    if cnt == 2:
        break