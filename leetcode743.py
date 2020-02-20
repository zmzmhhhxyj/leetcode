import collections
from typing import List
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = collections.defaultdict(list)
        for u,v,w in times:
            g[u].append((w,v))
        visited = set()
        distances = {i:float("inf") for i in range(1,N+1)}
        distances[K]=0
        heap = [(0,K)]
        while heap:
            dis,curid = heapq.heappop(heap)
            if curid in visited:
                continue
            visited.add(curid)
            if len(visited)==N:
                return distances[curid]
            for next_dis,nextid in g[curid]:
                if distances[curid]+next_dis < distances[nextid] and nextid not in visited:
                    heapq.heappush(heap,(distances[curid]+next_dis,nextid))
                    distances[nextid] = distances[curid]+next_dis
        return -1


a = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
x = Solution()
res = x.networkDelayTime(a,3,1)
print(res)
