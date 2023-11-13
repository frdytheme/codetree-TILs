arr = input().split()
list = [int(arr[0]), int(arr[1]), int(arr[2])]
a, b = sum(list), int(sum(list)/len(list))
print(f"{a}\n{b}\n{a-b}")