A, B, C = input().split(), input().split(), input().split()
a, b, c = A[0], B[0], C[0]
ac, bc, cc = int(A[1]), int(B[1]), int(C[1])

if a+b == "YY" or a+c == "YY" or b + c == "YY":
    if (a >= 36 and b >= 36) or (a >= 36 and c >= 36) or (b >= 36 and c >= 36):
        print("E")
else:
    print("N")