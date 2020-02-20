from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,mini = 0,prices[0]
        for price in prices:
            if price<mini:
                mini = price
            else:
                profit = max(price-mini,profit)
        return profit
        
x = Solution()
res = x.maxProfit([7,1,5,3,6,4])
print(res)