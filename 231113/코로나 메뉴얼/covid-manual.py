A, B, C = input().split(), input().split(), input().split()
a, b, c = A[0], B[0], C[0]
ac, bc, cc = int(A[1]), int(B[1]), int(C[1])

if a == "Y" and ac >= 37:
    if (b == "Y" and bc >= 37) or (c == "Y" and cc >= 37):
        print("E")
    else:
        print("N")
else:
    if (b == "Y" and bc >= 37) and (c == "Y" and cc >= 37):
        print("E")
    else:
        print("N")