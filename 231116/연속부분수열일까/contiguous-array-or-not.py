n1, n2 = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

check = False
idx = 0
for n in A:
    if n == B[idx]:
        check = True
        idx += 1
        if idx == len(B):
            break
    else:
        check = False
        idx = 0
if check:
    print("Yes")
else:
    print("No")