from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        win = self.maxChoice(nums,0,len(nums)-1)
        return win>=0

    def maxChoice(self,nums,l,r):
        if l==r:
            return nums[l]
        if self.dp[l][r]>0:
            return self.dp[l][r]
        else:
            self.dp[l][r] = max(nums[l]-self.maxChoice(nums,l+1,r),nums[r]-self.maxChoice(nums,l,r-1))
            return self.dp[l][r]

    def PredictTheWinner2(self, nums: List[int]) -> bool:
        win = self.maxChoice2(nums,0,len(nums)-1)
        return win>=0

    def maxChoice2(self,nums,l,r):
        if l==r:
            return nums[l]
        maxNum = max(nums[l]-self.maxChoice(nums,l+1,r),nums[r]-self.maxChoice(nums,l,r-1))
        return maxNum
        

a = [1, 5, 233, 7]
x = Solution()
ans = x.PredictTheWinner(a)
print(ans)