from  typing import List 
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if matrix is None or not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        self.dp = matrix
        for i in range(1,row):
            self.dp[i][0]=self.dp[i-1][0]+self.dp[i][0]
        for j in range(1,col):
            self.dp[0][j]=self.dp[0][j-1]+self.dp[0][j]
        for i in range(1,row):
            for j in range(1,col):
                self.dp[i][j] = self.dp[i-1][j]+self.dp[i][j-1]+self.dp[i][j]-self.dp[i-1][j-1]
        print(self.dp)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.dp[row2][col2]-self.dp[row1-1][col2]-self.dp[row2][col1-1]+self.dp[row1-1][col1-1]
        return ans


x = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
a = x.sumRegion(1,1,2,2)
print(a)
"""
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
"""