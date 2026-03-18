"""" .... nearest greater to right this is stack question.... """

arr = [2, 4, 3, 1, 7, 0] 

stack = [] 
result = [] 

for i in range(len(arr)-1 , -1, -1):
    
    while stack and stack[-1] <= arr[i] :
        stack.pop() 
        
    if not stack :
        result.append(-1) 
        
    else:
        result.append(stack[-1]) 
        
    stack.append(arr[i])

new_result = result[::-1]
print(new_result)
