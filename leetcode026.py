from typing import List
class Solution:
    def removeDuplicates(nums: List[int]) -> int:
        res=[]
        i=0
        while i<(len(nums)):
            res.append(nums[i])
            while(i<len(nums)-2 and nums[i]==nums[i+1]):
                i=i+1
            i=i+1
        return res

x = Solution()
a = Solution.removeDuplicates([1,1,2])
print(a)