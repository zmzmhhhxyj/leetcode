from typing import List
import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=1:
            return [0]
        g = collections.defaultdict(list)
        degrees = [0]*n
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
            degrees[edge[0]]+=1
            degrees[edge[1]]+=1
        leaves = [i for i in range(n) if degrees[i]==1]
        while leaves:
            tmp = []
            ans = leaves
            for leaf in leaves:
                for neighbor in g[leaf]:
                    degrees[neighbor]-=1
                    if degrees[neighbor]==1:
                        tmp.append(neighbor)
            leaves = tmp
        return ans

a = [[1,0],[1,2],[1,3]]
x = Solution()
res = x.findMinHeightTrees(4,a)
print(res)