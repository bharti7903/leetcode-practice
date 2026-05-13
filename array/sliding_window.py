arr = [100, 200, 300, 400] 
k = 2 
output = 700 
#explnation: arr2 + arr3 = 700, which is maximum 

i = 0 
j = 0 

sum = 0 
max_sum = 0 

while j < len(arr) :
    sum = sum + arr[j] 
    if (j-i+1) < k :
        j += 1  
        
    elif (j-i+1) == k :
        max_sum = max(max_sum, sum) 
        
        sum = sum - arr[i] 
        
        i += 1 
        j += 1 
    
print(max_sum)