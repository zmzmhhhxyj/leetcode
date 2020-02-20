from typing import List
import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = collections.defaultdict(dict)
        for (x,y),value in zip(equations,values):
            g[x][y] = value
            g[y][x] = 1.0/value
        ans = []
        for query in queries:
            a = query[0]
            b = query[1]
            if len(g[a])==0 or len(g[b])==0:
                ans.append(-1)
                continue
            visited = []
            ans.append(self.divide(g,a,b,visited))
        return ans


    def divide(self,g,a,b,visited): #a/b
        if a==b:
            return 1
        visited.append(a)
        for c in g[a]:
            if c in visited:
                continue
            res = self.divide(g,c,b,visited)#c/b
            if res>0:
                return g[a][c]*res #a/c*c/b
        return -1


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
x = Solution()
res = x.calcEquation(equations,values,queries)
print(res)