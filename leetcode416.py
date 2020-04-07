from typing import List
class Solution:
    #solution 1
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum%2!=0:
            return False
        return self.helper(0,nums_sum//2,nums)
    
    def helper(self,index,target,nums):
        if target==0:
            return True
        if index>len(nums)-1 or target<0:
            return False
        if self.helper(index+1,target-nums[index],nums):
            return True
        index+=1
        while index<len(nums) and nums[index]==nums[index-1]:
            index+=1
        return self.helper(index,target,nums)

    #solution 2
    def canPartition2(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum%2!=0:
            return False
        dp = [False]*nums_sum
        dp[0] = True
        for num in nums:
            for i in range(nums_sum//2,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
                if dp[nums_sum//2]:
                    return True
        return dp[nums_sum//2]

x = Solution()
print(x.canPartition([1, 5, 11, 5]))