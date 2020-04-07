from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                i+=2
            else:
                return nums[i]
        return nums[-1]
    

l = [2,2,1]
x= Solution()
res = x.singleNumber(l)
print(res) 