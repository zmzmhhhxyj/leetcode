from typing import List
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maxsub,count,minsub,curMax,curMin = -float("inf"),0,float("inf"),0,0
        for a in A:
            curMax = max(curMax+a,a)
            maxsub = max(curMax,maxsub)
            count+=a
            curMin = min(curMin+a,a)
            minsub = min(minsub,curMin)
        if maxsub<=0:
            return maxsub
        else:
            return max(maxsub,count-minsub)

x = Solution()
# res = x.maxSubarraySumCircular([1,-2,3,-2])
res = x.maxSubarraySumCircular([5,-3,5])
print(res)