from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(n,s,path):
            if n==len(path):
                res.append(path.copy())
                return
            for i in range(s,len(nums)):
                path.append(nums[i])
                dfs(n,i+1,path)
                path.pop()
            return res
        for n in range(len(nums)+1):
            dfs(n,0,[])
        return res


if __name__=="__main__":
    a = [1,2,3]
    x = Solution()
    res = x.subsets(a)
    print(res)