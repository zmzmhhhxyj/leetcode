from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(nums,0,[],res)
        return res
    def dfs(self,nums,pos,path,res):
        res.append(path)
        for i in range(pos,len(nums)):
            if i>pos and nums[i]==nums[i-1]:
                continue
            self.dfs(nums,i+1,path+[nums[i]],res)

a = [1,2,2]
x = Solution()
res = x.subsetsWithDup(a)
print(res)