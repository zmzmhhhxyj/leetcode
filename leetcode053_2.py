from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]*len(nums)
        max_dp = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            max_dp = max(max_dp,dp[i])
        return max_dp

x = Solution()
a = x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(a)