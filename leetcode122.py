from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1: return 0
        diff = [0]*(n-1)
        res = 0
        for i in range(n-1):
            diff[i] = prices[i+1]-prices[i]
        for i in range(n-1):
            if diff[i]>0:
                res+=diff[i]
        return res


x = Solution()
res = x.maxProfit([3,3,5,0,0,3,1,4])
print(res)