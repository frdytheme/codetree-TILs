string = input()

now_str = string[0]
cnt = 1
arr = []
for s in string[1:]:
    if s == now_str:
        cnt += 1
    else:
        arr.append(f"{now_str}{cnt}")
        now_str = s
        cnt = 1
arr.append(f"{now_str}{cnt}")

length = 0
result = ""
for s in arr:
    result += s
    length += len(s)
    
print(length)
print(result)