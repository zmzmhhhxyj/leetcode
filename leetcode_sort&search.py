from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        start,end = -1,-1
        l,r= 0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>=target:
                r = mid
            else:
                l = mid+1
        if nums[l]==target:
            start = l
        if start == -1:
            return [-1,-1]
        l,r= 0,len(nums)
        while l<r:
            mid = (l+r)//2
            if nums[mid]>target:
                r = mid
            else:
                l = mid+1
        end = l-1
        return [start,end]

x = Solution()
# ans = x.searchRange([5,7,7,8,8,10],8)
ans = x.searchRange([1],1)
print(ans)