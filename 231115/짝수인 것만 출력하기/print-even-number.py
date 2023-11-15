n = input()
arr = list(map(int, input().split()))
even = []
for n in arr:
    if n % 2 == 0:
        even.append(n)
for c in even:
    print(c, end=" ")