""" .... nearest greater to left stack coding question.... """ 

arr = [7, 3, 6, 4, 1, 0] 

stack = []
result = []   # -1, 7, 7, 6, 4, 1

for i in range(len(arr)) :
    while stack and stack[-1] <= arr[i] :
        stack.pop() 
        
    if not stack:
        result.append(-1) 
        
    else:
        result.append(stack[-1])
        
    stack.append(arr[i]) 
    
print(result)  
