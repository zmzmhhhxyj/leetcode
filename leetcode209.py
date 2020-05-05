from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l,r = 0,0
        count = 0
        length = float('inf')
        while r<len(nums):
            count+=nums[r]
            while l<=r and count>=s:
                length = min(length,r-l+1)
                count-=nums[l]
                l+=1
            r+=1
        return length if length!=float('inf') else 0

x = Solution()
# res = x.minSubArrayLen(7,[2,3,1,2,4,3])
res = x.minSubArrayLen(7,[1,1,1])
print(res)