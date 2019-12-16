class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for x in range(m)] for  x in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

x = Solution()
a = x.uniquePaths(7,3)
print(a)