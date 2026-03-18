nums = [4, 5, 6, 7, 0, 1, 2], target = 0 
#Output: 4 
#Explanation: The target value 0 is at index 4 in the rotated array.
# nums = [4, 5, 6, 7, 0, 1, 2], target = 3 
# Output: -1 
#Explanation: The target value 3 is not present in the array.

size = len(nums) 
index_1 = -1
for i in range(size): 
    if nums[i] == target :
        index_1 = i
        print(index_1) 
        
print(index_1)