A, B, C = input().split(), input().split(), input().split()
a, b, c = A[0], B[0], C[0]
ac, bc, cc = int(A[1]), int(B[1]), int(C[1])

if ac + bc >= 74 or ac + cc >= 74 or bc + cc >= 74:
    if a+b == "YY" or a+c == "YY" or b + c == "YY":
        print("E")
else:
    print("N")