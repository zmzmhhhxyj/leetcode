from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        bottom =0
        top = len(matrix[0])-1
        right = len(matrix[1])-1
        while left<right:
            self.swap(matrix,left,bottom,right,top)
            left = left+1
            bottom = bottom+1
            top = top-1
            right = right-1
        return matrix
    def swap(self,matrix,left,bottom,right,top):
        for i in range(right-left):
            tmp = matrix[bottom][left+i] #store the bottom side
            matrix[bottom][left+i]=matrix[top-i][left]
            matrix[top-i][left]=matrix[top][right-i]
            matrix[top][right-i]=matrix[bottom+i][right]
            matrix[bottom+i][right]=tmp

x = Solution()
a = x.rotate([[ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]])
print(a)