num = input().split()
a, b = int(num[0]), int(num[1])
val = 0
for i in range(a, b+1):
    if i % 2 == 0:
        val += i
print(val)