from  typing import List 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None: return None
        dp = [1]
        for i in range(1,len(nums)):
            max_num = 1
            for j in range(0,i):
                if nums[j]<nums[i] and dp[j]+1>max_num:
                    max_num = dp[j]+1
            dp.append(max_num)
        return max(dp)

x = Solution()
a = x.lengthOfLIS([10,9,2,5,3,7,101,18])
print(a)