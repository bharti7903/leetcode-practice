#arr = [5, 4, 3, 2, 1]
# Output: False
 
# arr = [1, 3, 2, 4, 5]
# Output: False
 
arr = [1, 2, 3, 4, 5]
# Output: True   

# with using built in function sorted() to check 

# new_arr = sorted(arr) 
# if new_arr == arr :
#     print(True) 
    

# else :
#     print(False)  

# without using built in function to check is array sorted 

n = len(arr) 
for i in range(n-1):
    if arr[i] > arr[i+1] :
        print(False) 
        break
        
else:
    print(True)
            