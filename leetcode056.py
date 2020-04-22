# 191117
# 200419
from typing import List
import collections
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        g = self.buildGraph(intervals)
        nodes_set,count = self.getConnected(g,intervals)
        return [self.start_end(nodes_set[i]) for i in range(count)]


    def buildGraph(self,intervals):
        g = collections.defaultdict(list)
        for i,l in enumerate(intervals):
            for j in range(i+1,len(intervals)):
                if l[0]<=intervals[j][1] and intervals[j][0]<=l[1]:
                    g[tuple(l)].append(intervals[j])
                    g[tuple(intervals[j])].append(l)
        return g

    def getConnected(self,g,intervals):
        visited = set()
        nodes_set = collections.defaultdict(list)
        count = 0
        def dfs(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_set[count].append(node)
                    stack.extend(g[node])
        for interval in intervals:
            if tuple(interval) not in visited:
                dfs(interval)
                count+=1
        return nodes_set,count

    def start_end(self,l):
        start = l[0][0]
        end = l[0][1]
        for node in l:
            start = min(start,node[0])
            end = max(end,node[1])
        return [start,end]


    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for l in intervals:
            if not merged or l[0]>merged[-1][1]: # no overlaps,append new interval
                merged.append(l)
            else:
                merged[-1][1] = max(merged[-1][1],l[1])
        return merged

x = Solution()
a = x.merge([[1,3],[2,6],[8,10],[15,18]])
print(a)