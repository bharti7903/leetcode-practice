nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
 
# Input: nums = [0, 0, 1]
# Output: [1, 0, 0]
 
# Input: nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
# Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]  

n = len(nums) 
pos = 0
for i in range(n) : 
    if nums[i] != 0 :
        nums[pos], nums[i] = nums[i], nums[pos] 
        
        pos += 1 
print(nums)