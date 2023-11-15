n, nn = 1, int(input())
stack = [n, nn]

while stack[-1] < 100:
    stack.append(stack[-1] + stack[-2])

for i in stack:
    print(i,end=" ")