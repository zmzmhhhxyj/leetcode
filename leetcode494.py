from typing import List
import collections
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        d = {0:1}
        for i in nums:
            tmp = collections.defaultdict(int)
            for k in d:
                tmp[k-i] += d[k]
                tmp[k+i] += d[k]
            d = tmp
        return d[S]

    def findTargetSumWays2(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        self.res = 0
        def dfs(idx,s):
            if idx==len(nums)-1:
                if s+nums[idx]==S:
                    self.res+=1
                if s-nums[idx]==S:
                    self.res+=1
                return
            dfs(idx+1,s+nums[idx])
            dfs(idx+1,s-nums[idx])
        dfs(0,0)
        return self.res

x = Solution()
# ans = x.findTargetSumWays([1],0)
ans = x.findTargetSumWays([1, 1, 1, 1, 1],3)
print(ans)