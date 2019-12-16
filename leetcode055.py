from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        i = 0
        cur_max=nums[0]
        while i<=max_idx:
            cur_max = i+nums[i]
            max_idx = max(cur_max,max_idx)
            i+=1
            if max_idx >= len(nums)-1:
                return True
        return False

x = Solution()
a = x.canJump([2,5,0,0])
print(a)