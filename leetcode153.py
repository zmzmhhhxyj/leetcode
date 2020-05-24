from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        res = nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                return nums[l]
            mid = (l+r)//2
            if nums[mid]>=nums[l]:
                res = min(res,nums[l])
                l = mid+1
            else:
                res = min(res,nums[mid])
                r = mid-1
        return res
    
x = Solution()
# ans = x.findMin([4,5,6,7,0,1,2])
# ans = x.findMin([3,4,5,1,2])
ans = x.findMin([2,1])
print(ans)