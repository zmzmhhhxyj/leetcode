from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float('inf') for _ in  range(len(triangle[-1])+1)] for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(0,i+1):
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        return min(dp[-1])

a = Solution()
res = a.minimumTotal([[-1],[3,2],[-3,1,-1]])
print(res)