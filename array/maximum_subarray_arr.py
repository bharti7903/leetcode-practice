arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
if not arr:
    print("0") 
    
    
current_arr = arr[0]
max_sum_arr = arr[0]
for i in range(1, len(arr)): 
    current_arr = (arr[i], current_arr + arr[i]) 
    max_sum_arr = max(max_sum_arr, current_arr)
        
print(max_sum_arr)
    
