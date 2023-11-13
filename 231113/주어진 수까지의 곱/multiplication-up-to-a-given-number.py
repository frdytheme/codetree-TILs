num = input().split()
a, b = int(num[0]), int(num[1])
val = 1
for i in range(a, b+1):
    val *= i
print(val)