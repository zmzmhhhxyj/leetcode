from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        tmp = sorted(nums)
        l, r = 0,len(nums)-1
        while l<=len(nums)-1:
            if nums[l]!=tmp[l]:
                break
            l+=1
        if l==len(nums):
            return 0
        while r>=0:
            if nums[r]!=tmp[r]:
                break
            r-=1
        return r-l+1
    
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        l, r = 0,len(nums)-1
        while l<len(nums)-1 and nums[l]<=nums[l+1]:
            l+=1
        while r>0 and nums[r]>=nums[r-1]:
            r-=1
        # when there are equal numbers in nums
        if l>r:
            return 0
        tmp = nums[l:r+1]
        s = min(tmp)
        b = max(tmp)
        while l>0 and nums[l-1]>s:
            l-=1
        while r<len(nums)-1 and nums[r+1]<b:
            r+=1
        return r-l+1

x = Solution()
# ans = x.findUnsortedSubarray([1,3,7,2,5,4,6,10])
ans = x.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
# ans = x.findUnsortedSubarray([1,2,3,3,3])
print(ans)