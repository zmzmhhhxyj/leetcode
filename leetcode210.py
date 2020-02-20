from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        for sublist in prerequisites:
            g[sublist[1]].append(sublist[0])
        visited = [0]*numCourses
        res = []
        for i in range(numCourses):
            circle_exist = self.findcircle(g,i,visited,res)
            if circle_exist:
                return []
        e = res[::-1]
        return e

    def findcircle(self,g,node,visited,res):
        if visited[node]==1:
            return False
        if visited[node]==-1:
            return True
        visited[node]=-1
        for neightbor in g[node]:
            if self.findcircle(g,neightbor,visited,res):
                return True
        visited[node] = 1
        res.append(node)
        return False

x = Solution()
#a = [[1,0],[2,0],[3,1],[3,2]]
a = [[0,1],[1,0]]
res = x.findOrder(2,a)
print(res)