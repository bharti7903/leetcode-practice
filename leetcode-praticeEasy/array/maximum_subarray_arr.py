arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
sum_arr = 0
max_sum_arr = 0 
for n in arr: 
    if sum_arr >= 0 :
        sum_arr += n 
        max_sum_arr = max(max_sum_arr, sum_arr) 
        
    else :
        sum_arr = 0 
        
print(max_sum_arr)
    
