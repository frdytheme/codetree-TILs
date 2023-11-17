A, B = input(), input()

cnt = 0
check = False
for i in range(len(A) - 1):
    A = A[-1] + A[:-1]
    cnt += 1
    if A == B:
        check = True
        break
        
if check:
    print(cnt)
else:
    print(-1)