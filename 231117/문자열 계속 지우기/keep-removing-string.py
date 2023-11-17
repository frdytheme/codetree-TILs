A, B = input(), input()
b_len = len(B)
while True:
    idx = A.find(B)

    if idx != -1:
        A = A[:idx] + A[idx+b_len:]
    else:
        break    
print(A)