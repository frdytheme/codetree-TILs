val = 0
cnt = 0

while True:
    n = int(input())
    if n // 10 != 2:
        break
    val += n
    cnt += 1
print(f"{(val / cnt):.2f}")