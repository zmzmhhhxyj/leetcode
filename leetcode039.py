from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(path,res,sum,start):
            if sum == target:
                res.append(path.copy())
                return
            if sum>target:
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                dfs(path,res,sum+candidates[i],i)
                path.pop()
                #path = path[:-1]
        dfs([],res,0,0)
        return res


x = Solution()
a = x.combinationSum([2,3,6,7],7)
print(a)

        