digits = [9, 9, 9]
# Output: [1, 2, 4]
 
# digits = [4, 3, 2, 1]
# Output: [4, 3, 2, 2]
 
# digits = [9, 9, 9]
# Output: [1, 0, 0, 0] 

n = len(digits) 
for i in range(n-1, -1, -1): 
    if digits[i] < 9 :
        digits[i] += 1 
        break
    digits[i] = 0
    
else:     
    digits = [1] + digits 
    
print(digits)