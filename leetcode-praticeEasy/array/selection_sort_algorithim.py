lst = [64, 25, 12, 22, 11]

size = len(lst) 
for i in range(0, size) :
    min_size = i
    for j in range(i+1, size):
        if lst[j] < lst[i]:
            min_size = j
            lst[j], lst[i] = lst[i], lst[j]  
            
print(lst)