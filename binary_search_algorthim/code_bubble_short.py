lst = [5, 1, 4, 2, 8] 

size = len(lst) 
if size == 0 :
    print(lst)
    
for passes in range(0, size): 
    for i in range(0, size-1-passes) :
        
        if lst[i] > lst[i+1] :
            lst[i], lst[i+1] = lst[i+1], lst[i]
            
        
print(lst)