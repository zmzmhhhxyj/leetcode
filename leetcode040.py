from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(path,res,start,sum):
            if sum==target:
                res.append(path.copy())
                return
            if sum>target:
                return
            for i in range(start,len(candidates)):
                if candidates[i]==candidates[i-1] and i>start:
                    continue
                path.append(candidates[i])
                dfs(path,res,i+1,sum+candidates[i])
                path.pop()
        dfs([],res,0,0)
        return res


x = Solution()
a = x.combinationSum([10,1,2,7,6,1,5],8)
print(a)

        