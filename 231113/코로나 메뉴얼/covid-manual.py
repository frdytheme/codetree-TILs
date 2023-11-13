A, B, C = input().split(), input().split(), input().split()
a, b, c = A[0], B[0], C[0]
ac, bc, cc = int(A[1]), int(B[1]), int(C[1])

if a+b == "YY" or a+c == "YY" or b + c == "YY":
    if (ac >= 37 and bc >= 37) or (ac >= 37 and cc >= 37) or (bc >= 37 and cc >= 37):
        print("E")
else:
    print("N")