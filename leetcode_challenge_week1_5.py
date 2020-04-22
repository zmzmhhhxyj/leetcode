from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                ans+=prices[i]-prices[i-1]
        return ans

a = [7,1,5,3,6,4]
x = Solution()
ans = x.maxProfit(a)
print(ans)