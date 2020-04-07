from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(n,start_idx,path,res):
            if len(path)==n:
                res.append(path.copy())
                return res
            for i in range(start_idx,len(nums)):
                if i>start_idx and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(n,i+1,path,res)
                path.pop()
        for i in range(len(nums)+1):
            dfs(i,0,[],res)
        return res

a = [1,2,2,2,3]
x = Solution()
res = x.subsetsWithDup(a)
print(res)