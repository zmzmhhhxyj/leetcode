# 200421
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        lo, hi = 0, len(nums)-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[lo]: #left part is ordered
                if target>=nums[lo] and target<=nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if target>=nums[mid] and target<=nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
        return -1
        
    def search2(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid+1
        # l is the smallest number in nums
        if target>=nums[l] and target<=nums[len(nums)-1]:
            start = l
            end = len(nums)-1
        else:
            start = 0
            end = l
        while start<=end:
            mid = (start+end)//2
            if nums[mid]<target:
                start = mid+1
            elif nums[mid]>target:
                end = mid-1
            else:
                return mid
        return -1


x = Solution()
a = x.search([4,5,6,7,0,1,2],0)
print(a)
