s = input().split('+')
nums = []

for x in s:
    nums.append(x)
    
nums = sorted(nums)

print(*nums,sep = "+")