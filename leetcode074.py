from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        i = 0
        j = len(matrix[0])-1
        while i < len(matrix) and j >=0 :
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:
                    i+=1
                elif matrix[i][j] > target:
                    j-=1
                    for k in range(j,-1,-1):
                        if matrix[i][k] == target:
                            return True
                    return False
        return False