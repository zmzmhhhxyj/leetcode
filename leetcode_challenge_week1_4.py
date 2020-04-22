from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0,0
        while r<len(nums)-1:
            if nums[l]!=0:
                l+=1
            r+=1
            if nums[r]!=0 and nums[l]==0:
                nums[r],nums[l] = nums[l],nums[r]
        return nums

a = [0,1,0,3,12]
x = Solution()
res = x.moveZeroes(a)
print(res)

                