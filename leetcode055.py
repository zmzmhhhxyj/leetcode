# 200421
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

    def canJump2(self, nums: List[int]) -> bool:
        if not nums:
            return False
        idx = len(nums)-2
        canReach = [False]*len(nums)
        canReach[len(nums)-1] = True
        while idx>=0:
            for gap in range(nums[idx],0,-1):
                if idx+gap>=len(nums)-1:
                    canReach[idx]=True
                    continue
                if canReach[idx+gap] == True:
                    canReach[idx]=True
                    continue
            idx-=1
        return canReach[0]

x = Solution()
a = x.canJump([2,5,0,0])
print(a)