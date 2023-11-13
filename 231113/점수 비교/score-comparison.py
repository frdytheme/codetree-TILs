A = input().split()
B = input().split()
Aa, Ab = int(A[0]), int(A[1])
Ba, Bb = int(B[0]), int(B[1])

print(f"{1 if Aa > Ba and Ab > Bb else 0}")