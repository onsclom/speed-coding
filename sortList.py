n = int(input())
nums = []
for i in range(n):
    x = int(input())
    nums.append(x)
    
nums = sorted(nums, reverse=True)

for x in range(0, len(nums)-1, 1):
    print(nums[x], end=" ")
    
print(nums[len(nums)-1])
