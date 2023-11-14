n = int(input())
i = 1
cnt = 0

while n > 1:
    cnt += 1
    if n / i > 1:
        n //= i
        i += 1
    else:
        break
print(cnt)