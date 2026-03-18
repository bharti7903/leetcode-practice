nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
# Output: []
 
# nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]
 
# nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4]   

# lst = []
# n1 = len(nums1) 
# n2 = len(nums2)
# for i in range(n1):
#     for j in range(n2): 
#         if nums1[i] == nums2[j] :
#             if nums1[i] not in lst:
#                 lst.append(nums1[i]) 
                
# print(lst)
              
set1 = set(nums1)
result = []

for num in nums2:
    if num in set1 and num not in result:
        result.append(num)

print(result)