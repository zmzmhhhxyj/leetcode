from typing import List
import collections
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False
        g = collections.defaultdict(list)
        for i in range(len(rooms)):
            g[i] = rooms[i]
        self.visited = []
        return self.helper(0,g)
        
    def helper(self,loc,g):
        self.visited.append(loc)
        if len(self.visited)==len(g):
            return True
        for neighbor in g[loc]:
            if neighbor in self.visited:
                continue
            if self.helper(neighbor,g):
                return True
        return False
    
x = Solution()
res = x.canVisitAllRooms([[1],[1,1]])
print(res)