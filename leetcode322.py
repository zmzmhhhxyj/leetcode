# 200421
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[-1] if dp[-1]<=amount else -1
        

coins = [1, 2, 5]
coins = [2]
x = Solution()
ans = x.coinChange(coins,3)
print(ans)