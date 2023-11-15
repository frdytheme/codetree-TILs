n = int(input())

# i가 짝수 => n에서 1씩 줄어듬, 홀수면 1씩 증가하며 출력하고 상하 대칭

for i in range(n):
    if i % 2 == 0:
        for _ in range(n - (i // 2)):
            print("*",end=" ")
        print()
    else:
        for _ in range((i + 1) // 2):
            print("*",end=" ")
        print()

for i in range(n, 0, -1):
    if i % 2 != 0:
        for _ in range(n - (i // 2)):
            print("*",end=" ")
        print()
    else:
        for _ in range((i + 1) // 2):
            print("*",end=" ")
        print()