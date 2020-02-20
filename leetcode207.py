from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for sublist in prerequisites:
            adj[sublist[0]].append(sublist[1])
        status = [0]*numCourses # 0 for unvisited, 1 for visited, -1 for visiting
        for i in range(numCourses):
            if self.hascycle(adj,i,status):
                return False
        return True
    
    def hascycle(self,adj,node,status):
        if status[node] == 1:
            return False
        if status[node] == -1:
            return True
        status[node] = -1
        for i in adj[node]:
            if self.hascycle(adj,i,status):
                return True
        status[node] = 1
        return False

x = Solution()
#a = [[1,0],[2,6],[1,7],[6,4],[7,0],[6,5]]
a = [[0,1],[1,0]]
res = x.canFinish(2,a)
print(res)