n = int(input())

count = 1

for x in range(n):
    nums = []
    for y in range(x+1):
        nums.append(count)
        count+=1
    print(*nums)