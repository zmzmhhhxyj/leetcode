class Solution(object):
    def maxProfit(self, prices):
        # dynamic programming
        n = len(prices)
        if n<=1: return 0
        mi = prices[0]
        l,r = [0]*n,[0]*n
        for i in range(1,n):
            l[i] = max(prices[i]-mi,l[i-1])
            mi = min(prices[i],mi)
        ma = prices[n-1]
        for i in range(n-2,-1,-1):
            r[i] = max(ma-prices[i],r[i+1])
            ma = max(prices[i],ma)
        res = max(l[n-1],r[0])
        for i in range(1,n-2):
            res = max(res,l[i]+r[i+1])
        return res

x = Solution()
res = x.maxProfit([3,3,5,0,0,3,1,4])
print(res)