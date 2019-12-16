from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        for i in sorted(intervals,key= lambda i:i[0]):
            if out and i[0]<=out[-1][1]:
                out[-1][1] = max(i[1],out[-1][1])
            else:
                out += [i]
        return out

x = Solution()
a = x.merge([[1,3],[2,6],[8,10],[15,18]])
print(a)