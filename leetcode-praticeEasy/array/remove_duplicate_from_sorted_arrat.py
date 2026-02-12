nums = [0,0,1,1,1,2,2,3,3,4]  

i = 0 
""" is just counting of unique number and take one step foreward i as equal to the place value of j 
    and you just imagine that nums is update but it actual not

"""
for j in range(1, len(nums)) :
    if nums[i] != nums[j] :
        i += 1 
        nums[i] = nums[j] 
        
i += 1
    
print(i) 

        
    