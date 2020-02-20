import collections
from typing import List
class Solution:
    ##first solution
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+1)]
        sizes = [1]*(len(edges)+1)
        for edge in edges:
            start = edge[0]
            end = edge[1]
            p_start = self.find(parents,start)
            p_end = self.find(parents,end)
            if p_start==p_end:
                return edge
            if sizes[p_start]>sizes[p_end]:
                p_start,p_end = p_end,p_start
            parents[p_start] = p_end
            sizes[p_end]+=sizes[p_start]
        return -1

    def find(self,parents,node):
        while node!=parents[node]:
            parents[node] = parents[parents[node]]
            node = parents[node]
        return node

    ##second solution
    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for edge in edges:
            start = edge[0]
            end = edge[1]
            visited = [False]*(len(edges)+1)
            if self.haspath(graph,start,end,visited):
                return edge
            graph[start].append(end)
            graph[end].append(start)
        return -1

    def haspath(self,graph,start,end,visited):
        if start == end:
            return True
        visited[start]=True
        for neighbor in graph[start]:
            if visited[neighbor]:
                continue
            if self.haspath(graph,neighbor,end,visited):
                return True
        return False

a = [[1,2], [2,3], [3,4], [1,4], [1,5]]
x = Solution()
res = x.findRedundantConnection(a)
print(res)
