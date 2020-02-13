import collections
import numpy as np
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        q = collections.deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    grid[i][j]=2
                    q.append((i,j))
                    count += 1
                    self.bfs(grid,q)
        return count
    
    def bfs(self,grid,q):
        while q:
            i,j = q.pop()
            if 0<=i-1<len(grid) and grid[i-1][j]==1:
                grid[i-1][j]=2
                q.append((i-1,j))
            if 0<=i+1<len(grid) and grid[i+1][j]==1:
                q.append((i+1,j))
                grid[i+1][j]=2
            if 0<=j-1<len(grid[0]) and grid[i][j-1]==1:
                q.append((i,j-1))
                grid[i][j-1]=2
            if 0<=j+1<len(grid[0]) and grid[i][j+1]==1:
                q.append((i,j+1))
                grid[i][j+1]=2
        return

x = Solution()
a = np.array([1,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1])
a = np.reshape(a,(4,5))
res = x.numIslands(a)
print(res)