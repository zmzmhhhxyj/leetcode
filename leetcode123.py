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

    def maxProfit2(self, prices):
        # dynamic programming
        # 200518
        if len(prices)<=1:
            return 0
        p1 = [0]*len(prices)
        p2 = [0]*len(prices)
        left_curmin = prices[0]
        right_curmax = prices[-1]
        l_diff = 0
        r_diff = 0
        for i in range(len(prices)):
            l_diff = max(l_diff,prices[i]-left_curmin)
            left_curmin = min(left_curmin,prices[i])
            p1[i] = l_diff
        for i in range(len(prices)-1,-1,-1):
            r_diff = max(r_diff,right_curmax-prices[i])
            right_curmax = max(right_curmax,prices[i])
            p2[i] = r_diff
        res = max(p1[-1],p2[0])
        for i in range(0,len(prices)-1):
            res = max(res,p1[i]+p2[i+1])
        return res

x = Solution()
res = x.maxProfit([3,3,5,0,0,3,1,4])
print(res)