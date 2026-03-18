lst = [5, 1, 4, 2, 8]  
size = len(lst) 
if size == 0 :
    print(lst) 
    
for i in range(0, size) :
    for j in range(size-1-i, 0, -1) :
        if lst[j] < lst[j-1] :
            lst[j], lst[j-1] = lst[j-1], lst[j]  
            print(lst)
            
print(lst)
