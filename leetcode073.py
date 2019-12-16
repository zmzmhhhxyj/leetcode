from typing import List
class Solution(object):
    def setZeroes(self, matrix):
        mask = -1
        clear = False
        for i in range(len(matrix)):
            clear = False
            for j in range(len(matrix[0])):
                if  matrix[i][j] == 0:
                    if mask==-1:
                        mask = i
                        for k in range(len(matrix[0])):
                            matrix[mask][j] = 1 if matrix[mask][j]!=0 else 0
                        break
                    else:
                        matrix[mask][j]=0
                        clear = True
            if clear == True:
                matrix[i] = [0]*len(matrix[0])
        if mask == -1:
            return matrix
        else:
            for i in range(len(matrix[0])):
                if matrix[mask][i] == 0:
                    for j in range(len(matrix)):
                        matrix[j][i] = 0
        matrix[mask] = [0]*len(matrix[0])
        return matrix

x = Solution()
a = x.setZeroes([
  [5,1,2,0],
  [3,0,5,2],
  [1,3,1,5]
])
print(a)
