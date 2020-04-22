class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # if len(matrix) and len(matrix[0])<=1:
        #     if matrix[0]==target:
        #         return True
        #     else:
        #         return False
        i = len(matrix)-1 
        j = 0
        while i>=0 and j<=len(matrix[0])-1:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]>target:
                i-=1
            else:
                j+=1
        return False
    
a = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
a = [[1]]
x = Solution()
ans = x.searchMatrix(a,1)
print(ans)