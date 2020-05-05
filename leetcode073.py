from typing import List
class Solution(object):
    def setZeroes(self, matrix):
        mask = -1 #第一次出现0的行数
        clear = False
        for i in range(len(matrix)):
            clear = False
            for j in range(len(matrix[0])):
                if  matrix[i][j] == 0:
                    if mask==-1:
                        mask = i
                        # for k in range(len(matrix[0])):
                        #     matrix[mask][j] = 1 if matrix[mask][j]!=0 else 0 #保留mask行的0 #不需要也ok
                        break
                    else:
                        matrix[mask][j]=0 #在mask列记录j列，将来清空
                        clear = True #当前行清空
            if clear == True:
                matrix[i] = [0]*len(matrix[0])
        if mask == -1: #没有出现0，直接返回
            return matrix
        else: #出现0，遍历mask行对相应列清空
            for i in range(len(matrix[0])):
                if matrix[mask][i] == 0:
                    for j in range(len(matrix)):
                        matrix[j][i] = 0
        matrix[mask] = [0]*len(matrix[0])
        return matrix

x = Solution()
a = x.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
print(a)
