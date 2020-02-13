from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs([-1]*n,0,[],res)
        return res
    
    def dfs(self,nums,row,path,res):
        if row==len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[row]=i
            if self.trueQueen(nums,row):
                self.dfs(nums,row+1,path+["."*i+"Q"+"."*(len(nums)-i-1)],res)
    
    def trueQueen(self,nums,i):
        for j in range(i):
            if nums[j]==nums[i]:
                return False
            if abs(nums[j]-nums[i])==i-j:
                return False
        return True

x = Solution()
res = x.solveNQueens(4)
print(res)
