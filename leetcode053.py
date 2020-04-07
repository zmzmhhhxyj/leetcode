from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    def maxSubArray2(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i],nums[i-1]+nums[i])
            ans = max(nums[i],ans)
        return ans

    def maxSubArray3(self, nums: List[int]) -> int:
        ans = self.merge(nums,0,len(nums)-1)
        return ans

    def merge(self,nums,l,r):
        if l==r:
            return nums[l]
        mid = (l+r)//2
        return max(max(self.merge(nums,l,mid),self.merge(nums,mid+1,r)),self.crossMid(nums,l,mid,r))
    
    def crossMid(self,nums,l,mid,r):
        ans = 0
        ans_l = nums[mid]
        idx = mid
        while idx>=l:
            ans = ans + nums[idx]
            ans_l = max(ans,ans_l)
            idx -= 1

        ans = 0
        ans_r = nums[mid+1]
        idx = mid+1
        while idx<=r:
            ans = ans + nums[idx]
            ans_r = max(ans_r,ans)
            idx += 1
        return ans_l+ans_r
    

x = Solution()
a = x.maxSubArray3([-2,1,-3,4,-1,2,1,-5,4])
print(a)