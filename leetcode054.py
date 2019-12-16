from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return matrix
        bottom = 0
        left = 0 
        top = len(matrix)-1
        right = len(matrix[0])-1
            
        res = []
        while left<right and bottom<top:
            j = left
            i = bottom
            while j<right:
                res.append(matrix[i][j])
                j = j+1
            while i<top:
                res.append(matrix[i][j])
                i = i+1
            while j>left:
                res.append(matrix[i][j])
                j = j-1
            while i>bottom:
                res.append(matrix[i][j])
                i = i-1
            bottom = bottom+1
            right = right-1
            top = top-1
            left = left+1
        if left<right:
            for i in range(left,right+1):
                res.append(matrix[bottom][i])
        elif bottom<top:
            for i in range(bottom,top+1):
                res.append(matrix[i][left])
        else:
            for i in range(left,right+1):
                res.append(matrix[bottom][i])
        return res

x = Solution()
a = x.spiralOrder([[1,2],[3,4]])
print(a)
            



