from typing import List
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        dp = [[float('inf') for _ in range(len(A[0])+2)] for _ in range(len(A))]
        dp[0][1:-1] = A[0][:]
        for i in range(1,len(A)):
            for j in range(1,len(A)+1):
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])+A[i][j-1]
        return min(dp[-1])
        
x = Solution()
ans  = x.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])
print(ans)