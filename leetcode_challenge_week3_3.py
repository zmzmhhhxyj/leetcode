import collections
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = collections.deque()
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    q.append((r,c))
                    grid[r][c] = "2"
                    ans+=1
                    while q:
                        i,j = q.popleft()
                        if i>0 and grid[i-1][j]=="1":
                            q.append((i-1,j))
                            grid[i-1][j]="2"
                        if i<len(grid)-1 and grid[i+1][j]=="1":
                            q.append((i+1,j))
                            grid[i+1][j]="2"
                        if j>0 and grid[i][j-1]=="1":
                            q.append((i,j-1))
                            grid[i][j-1]="2"
                        if j<len(grid[0])-1 and grid[i][j+1]=="1":
                            q.append((i,j+1))
                            grid[i][j+1]="2"
        return ans

a = [["1","1","1"],["0","1","0"],["0","1","0"]]
x = Solution()
ans = x.numIslands(a)
print(ans)