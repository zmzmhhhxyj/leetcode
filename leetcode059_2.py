from typing import List
class Solution:
    def generateMatrix(self, n): 
        """ 
        :type n: int
        :rtype: List[List[int]]
        """
        x,y = 0,0
        idx_dir = 0
        d = ((0,1),(1,0),(0,-1),(-1,0))
        matrix = [[0 for i in range(n)] for _ in range(n)]
        for i in range(1,n**2+1):
            matrix[y][x] = i
            new_x = x+d[idx_dir][1]
            new_y = y+d[idx_dir][0]
            if new_x>n-1 or new_y>n-1 or matrix[new_y][new_x]!=0:
                idx_dir = (idx_dir+1)%4
            x += d[idx_dir][1]
            y += d[idx_dir][0]
        return matrix



x = Solution()
a = x.generateMatrix(3)
print(a)