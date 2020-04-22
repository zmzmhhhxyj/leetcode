from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def smash(stones):
            if len(stones)==1:
                self.ans = stones[0]
                return
            if len(stones)==0:
                return
            stones.sort()
            if stones[-1]!=stones[-2]:
                stones[-2] = stones[-1]-stones[-2]
                stones = stones[:-1]
            else:
                stones = stones[:-2]
            self.lastStoneWeight(stones)
            return
        self.ans = 0
        smash(stones)
        return(self.ans)
        

x = Solution()
res = x.lastStoneWeight([1,2,6,20])
print(res)