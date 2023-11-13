num = input().split()
a, b = int(num[0]), int(num[1])
val = 0
cnt = 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        val += i
        cnt += 1
print(f"{val} {val / cnt:.1f}")