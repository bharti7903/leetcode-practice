
from typing import List
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0 
        n = len(arr) 
        for i in range(n) :
            for j in range(i+1, n) :
                for k in range(j+1, n) :
                    if arr[i] - arr[j] <= a and arr[j] - arr[k] <= b and arr[k] - arr[i] <= c :
                        count += 1 

                    

        return count 
    
obj = Solution()
result = obj.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3)
print(result)
    
