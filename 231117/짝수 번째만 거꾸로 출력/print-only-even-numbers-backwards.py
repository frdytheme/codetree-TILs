s = input()
arr = []

for i,c in enumerate(s):
    if i % 2 != 0:
        arr.append(c)

for s in arr[::-1]:
    print(s, end="")