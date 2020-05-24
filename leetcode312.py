from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)
        nums.append(1)
        dp = [[0 for _ in range(len(nums))]for _ in range(len(nums))]
        for l in range(1,len(nums)-1):
            for i in range(1,len(nums)-l):
                j = i+l-1
                for k in range(i,j+1):
                    dp[i][j] = max(dp[i][j],nums[i-1]*nums[k]*nums[j+1]+dp[i][k-1]+dp[k+1][j])                
        return dp[1][len(nums)-2]
        

x = Solution()
ans = x.maxCoins([3,1,5,8])
print(ans)