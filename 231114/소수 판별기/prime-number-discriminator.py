n = int(input())
check = True

for i in range(2, n // 2):
    if n % i == 0:
        check = False
        break
if check:
    print("P")
else:
    print("C")