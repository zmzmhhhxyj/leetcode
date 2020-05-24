from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 0
        r = len(dungeon)
        c = len(dungeon[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[-1][-1] = max(1,1-dungeon[-1][-1])
        for i in range(r-2,-1,-1):
            dp[i][c-1] = max(dp[i+1][c-1]-dungeon[i][c-1],1)
        for i in range(c-2,-1,-1):
            dp[r-1][i] = max(dp[r-1][i+1]-dungeon[r-1][i],1)
        for i in range(r-2,-1,-1):
            for j in range(c-2,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        return dp[0][0]

x = Solution()
a = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
ans = x.calculateMinimumHP(a)
print(ans)