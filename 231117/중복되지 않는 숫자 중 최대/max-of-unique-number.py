n = int(input())
num = list(map(int, input().split()))

max_num = -1

for n in num:
    if max_num < n:
        count = 0
        for i in num:
            if i == n:
                count += 1
        if count == 1:
            max_num = n
print(max_num)