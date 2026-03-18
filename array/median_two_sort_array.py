from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1 = nums1 + nums2
        list1.sort()
        length = len(list1) 
        if length%2 == 0 :
            med = length//2 
             
            median = (list1[med-1] + list1[med])/2
        else : 
            med = length//2 
            median = list1[med]
        return median

obj = Solution()
result = obj.findMedianSortedArrays([1, 3], [2])
print(result)