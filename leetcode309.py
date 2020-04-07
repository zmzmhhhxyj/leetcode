from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<2:
            return 0
        hold = [0]*n
        unhold = [0]*n
        hold[0] = -prices[0]
        hold[1] = max(-prices[0],-prices[1])
        for i in range(1,len(prices)):
            if i>1:
                hold[i] = max(hold[i-1],unhold[i-2]-prices[i])
            unhold[i] = max(unhold[i-1],hold[i-1]+prices[i])
        return unhold[n-1]

a = [1,2,3,0,2]
x = Solution()
res = x.maxProfit(a)
print(res)
