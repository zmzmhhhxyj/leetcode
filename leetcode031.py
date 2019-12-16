from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i,j = len(nums)-1,len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i=i-1
        if i==0:
            nums.reverse()
            return nums
        k = i-1
        while nums[j]<=nums[k]:
            j=j-1
        nums[k],nums[j]=nums[j],nums[k]
        l=k+1
        r=len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l=l+1
            r=r-1
        return nums

x = Solution()
a = x.nextPermutation([1,5,1])
print(a)
