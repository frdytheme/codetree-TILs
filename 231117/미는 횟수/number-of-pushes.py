A, B = input(), input()

cnt = 0

while A != B:
    A = A[-1] + A[:-1]
    cnt += 1
    
print(cnt)