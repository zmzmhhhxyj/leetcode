from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                #res.append(matrix.pop()[::-1])
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res

x = Solution()
a = x.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
            



