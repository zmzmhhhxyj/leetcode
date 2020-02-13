from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = [1]*len(nums)
        down = [1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                up[i] = down[i-1]+1
                down[i] = down[i-1]
            elif nums[i]<nums[i-1]:
                down[i] = up[i-1]+1
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
        return max(up[-1],down[-1])

x = Solution()
res = x.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
print(res)