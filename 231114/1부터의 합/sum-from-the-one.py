n = int(input())
val = 0
for i in range(1, 101):
    if val + i >= n:
        break
    val += i

print(val)