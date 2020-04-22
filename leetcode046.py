# needs review
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path,res):
            if len(path)==len(nums):
                res.append(path.copy())
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(path,res)
                path.pop()
            return res
        return dfs([],res)


x = Solution()
a = x.permute([1,2,3])
print(a)