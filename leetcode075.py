from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums)-1
        cur = 0
        while cur<=r:
            if nums[cur]==0:
                if l<cur:
                    nums[cur],nums[l] = nums[l],nums[cur]
                    l += 1
                else:
                    l+=1
                cur+=1
            elif nums[cur]==1:
                cur+=1
            elif nums[cur]==2:
                nums[r],nums[cur]=nums[cur],nums[r]
                r-=1


x = Solution()
nums = [2,0,1]
x.sortColors(nums)
print(nums)