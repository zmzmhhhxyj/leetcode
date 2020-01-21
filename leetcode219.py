from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i,val in enumerate(nums):
            if val in dic and i-dic[val]<=k:
                return True
            else:
                dic[val] = i
        return False

x = Solution()
res = x.containsNearbyDuplicate([1,2,3,1],3)
print(res)