from typing import List
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = collections.defaultdict(list)
        for ticket in tickets:
            g[ticket[0]]+=(ticket[1]),
        self.res = ["JFK"]
        def visit(loc):
            if len(self.res)==len(tickets)+1:
                return True
            dests = sorted(g[loc])
            for dest in dests:
                g[loc].remove(dest)
                self.res.append(dest)
                if visit(dest):
                    return True
                g[loc].append(dest)
                self.res.pop()
            return False
        visit("JFK")
        return self.res

a = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
x = Solution()
res = x.findItinerary(a)
print(res)

            
