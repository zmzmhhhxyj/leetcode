from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        #for i in range(len(nums)):
        self.helper(nums,0,res,[])
        return res
    def helper(self,nums,i,res,path):
        res.append(path)
        for i in range(i,len(nums)):
            self.helper(nums,i+1,res,path+[nums[i]])

if __name__=="__main__":
    a = [1,2,3]
    x = Solution()
    res = x.subsets(a)
    print(res)