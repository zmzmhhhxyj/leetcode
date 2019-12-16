from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        self.dfs(candidates,0,0,target,[],res)
        return res
    def dfs(self,candidates,idx,cur_num,target,cur_path,res):
        if cur_num==target:
            res.append(cur_path)
            return
        for i in range(idx,len(candidates)):
            if i>idx and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                return
            self.dfs(candidates,i+1,cur_num+candidates[i],target,cur_path+[candidates[i]],res)


x = Solution()
a = x.combinationSum([10,1,2,7,6,1,5],8)
print(a)

        