A = input().split()
B = input().split()
Aa, Ab = int(A[0]), int(A[1])
Ba, Bb = int(B[0]), int(B[1])

if Aa > Ba:
    print("A")
elif Ba > Aa:
    print("B")
elif Ab > Bb:
    print("A")
else:
    print("B")