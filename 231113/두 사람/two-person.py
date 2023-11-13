A = input().split()
B = input().split()

a_age, a = int(A[0]), A[1]
b_age, b = int(B[0]), B[1]

print(int((a_age >= 19 and a == "M") or (b_age >= 19 or b == "M")))