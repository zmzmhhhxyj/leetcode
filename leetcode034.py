from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1
        id1,id2=-1,-1
        while(l<=r):
            mid=l+(r-l)//2
            if target==nums[mid]:
                id1=mid
                r=mid-1
            elif(target<nums[mid]):
                r=mid-1
            elif(target>nums[mid]):
                l=mid+1
        r=len(nums)-1
        while(l<=r):
            mid=l+(r-l)//2
            if(target==nums[mid]):
                id2=mid
                l=mid+1
            elif(target<nums[mid]):
                r=mid-1
            elif(target>nums[mid]):
                l=mid+1
        return [id1,id2]

x = Solution()
a = x.searchRange([1],1)
print(a)