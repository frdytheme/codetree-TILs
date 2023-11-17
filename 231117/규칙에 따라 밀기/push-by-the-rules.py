A, B = input(), input()

for q in B:
    if q == "L":
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]
print(A)