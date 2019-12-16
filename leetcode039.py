from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        self.dfs(candidates,0,0,target,[],res)
        return res
    def dfs(self,candidates,idx,cur_num,target,cur_path,res):
        if cur_num>target:
            return
        if cur_num==target:
            res.append(cur_path)
            return
        for i in range(idx,len(candidates)):
            self.dfs(candidates,i,cur_num+candidates[i],target,cur_path+[candidates[i]],res)

x = Solution()
a = x.combinationSum([2,3,6,7],7)
print(a)

        