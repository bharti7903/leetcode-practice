
# """"
# LeetCode allow nahi karta new array banana
# modify the original array in-place
# i = 0 

# for j in range(len(nums)) :
#     if nums[j] != val :
#         nums[i] = nums[j] 
#         i += 1 

# return i

# """"

nums = [0,1,2,2,3,0,4,2]
val = 2 
new_nums = []

for i in range(len(nums)) :
    if nums[i] == val :
        continue 
    else :
        new_nums.append(nums[i]) 
print(new_nums)        

j = 0
        
for k in range(1, len(new_nums)) :
    if new_nums[j] != new_nums[k] :
        j += 1 
        new_nums[j] = new_nums[k] 
        
print(j+1)
