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
    
    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(l,idx,res,preNum,path):
            if len(path)==l:
                res.append(path.copy())
                return
            preNum = nums[0]-1
            for i in range(idx,len(nums)):
                if nums[i]!=preNum:
                    path.append(nums[i])
                    preNum = nums[i]
                    dfs(l,i+1,res,preNum,path)
                    # dfs(l,i+1,res,nums[i],path) 用这句替换上面两行居然是错的，递归真是麻烦
                    path.pop()
        for i in range(len(nums)+1):
            dfs(i,0,res,nums[0]-1,[])
        return res

a = [1,2,2,2,3]
a = [1,2,2]
x = Solution()
res = x.subsetsWithDup2(a)
print(res)