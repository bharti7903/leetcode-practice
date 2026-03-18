nums = [3, 0, 1]
#Output: 2

n = len(nums) 
missing_num = n*(n+1)//2 - sum(nums)
print(missing_num)