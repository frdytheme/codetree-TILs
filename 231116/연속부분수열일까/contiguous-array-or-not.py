n1, n2 = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 4 4 1 4
# 4 3

for i in range(n1):
    check = True
    for j in range(n2):
        if i + j >= n1:
            check = False
            break
        if A[i+j] != B[j]:
            check = False
            break
    if check:
        print("Yes")
        break
print("No")