from typing import List
class Solution:
    def maxProfit2(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        for i in range(1,k+1):
            maxdiff = -float('inf')
            for j in range(1,len(prices)):
                maxdiff = max(maxdiff,dp[i-1][j-1]-prices[j-1])
                dp[i][j] = max(dp[i][j-1],prices[j]+maxdiff)
        return dp[-1][-1]
        
    def maxProfit3(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0 for _ in range(len(prices))] for _ in range(2)]
        for i in range(1,k+1):
            maxdiff = -float('inf')
            dp[0][:] = dp[1][:]
            for j in range(1,len(prices)):
                maxdiff = max(maxdiff,dp[0][j-1]-prices[j-1])
                dp[1][j] = max(dp[1][j-1],prices[j]+maxdiff)
        return dp[-1][-1]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        if k>=len(prices)//2:
            res = 0
            for i in range(1,len(prices)):
                if prices[i]>prices[i-1]:
                    res+=prices[i]-prices[i-1]
            return res
        dp = [[0 for _ in range(len(prices))] for _ in range(2)]
        for i in range(1,k+1):
            maxdiff = -float('inf')
            dp[0][:] = dp[1][:]
            for j in range(1,len(prices)):
                maxdiff = max(maxdiff,dp[0][j-1]-prices[j-1])
                dp[1][j] = max(dp[1][j-1],prices[j]+maxdiff)
        return dp[-1][-1]

prices = [2,5,7,1,4,3,1,3]
# prices = [3,3,5,0,0,3,1,4]
x = Solution()
ans = x.maxProfit(7,prices)
print(ans)