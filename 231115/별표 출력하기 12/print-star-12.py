n = int(input())

for i in range(n):
    # for j in range((i + 1) * 2):
    #     print(end=" ")
    for j in range(n):
        if j < i:
            print(" ", end=" ")
        else:
            if j % 2 != 0 or i == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()