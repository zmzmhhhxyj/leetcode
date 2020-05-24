from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(path,res,prenum,used):
            if len(path)==len(nums):
                res.append(path.copy())
                return
            prenum = nums[0]-1
            for i in range(len(nums)):
                if nums[i]==prenum or used[i]==True:
                    continue 
                prenum = nums[i]
                used[i]=True
                path.append(nums[i])
                dfs(path,res,prenum,used)
                path.pop()
                used[i] = False
            return res
        return dfs([],res,nums[0]-1,[False]*len(nums))

a = [1,2,2]
x = Solution()
res = x.permuteUnique(a)
print(res)