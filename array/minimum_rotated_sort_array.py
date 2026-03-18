nums = [4, 5, 6, 7, 0, 1, 2] 
#Output: 0 


size = len(nums)
     
for i in range(0, size-1) :
    
    if nums[i] > nums[i+1] :
        
        print(nums[i+1]) 
        
        
print(nums[0])
        