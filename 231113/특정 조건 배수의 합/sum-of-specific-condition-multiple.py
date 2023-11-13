num = input().split()
a, b = int(num[0]), int(num[1])
val = 0
if b > a:
    for i in range(a, b+1):
        if i % 5 == 0:
            val += i
else:
    for i in range(b, a+1):
        if i % 5 == 0:
            val += i
print(val)