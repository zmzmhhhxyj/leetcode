from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        while(lo<=hi):
            mid = int((lo+hi)/2)
            if(nums[mid]==target):
                return mid
            if(nums[lo]<=nums[mid]):#左边有序
                if target>=nums[lo] and target<=nums[mid]:
                    hi=mid-1
                else:
                    lo=mid+1
            else:#右边有序
                if target>=nums[mid] and target<=nums[hi]:
                    lo=mid+1
                else:
                    hi=mid-1
        return -1

x = Solution()
a = x.search([7,8,9,0,1,2,4,6],1)
print(a)
