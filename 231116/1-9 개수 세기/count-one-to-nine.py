n = int(input())
arr = [0] * 9
nums = list(map(int,input().split()))

for i in nums:
    arr[i-1] += 1
for j in arr:
    print(j)