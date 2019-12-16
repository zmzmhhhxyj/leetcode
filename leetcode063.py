from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        dp = [[1 for x in range(m)] for  x in range(n)]
        dp[0][0] = 1-obstacleGrid[0][0]
        for i in range(1,m):
            dp[0][i] = (1-obstacleGrid[0][i])*dp[0][i-1]
        for i in range(1,n):
            dp[i][0] = (1-obstacleGrid[i][0])*dp[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

x = Solution()
a = x.uniquePathsWithObstacles([[1,0]])
print(a)