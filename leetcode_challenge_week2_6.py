# 20200414
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = dict()
        dic[0] = -1
        count = 0
        res = 0
        for i,num in enumerate(nums):
            if num==0:
                count-=1
            else:
                count+=1
            if count in dic:
                res = max(res,i-dic[count])
            else:
                dic[count] = i
        return res

a = [0,0,1,0,0,0,1,1]
a = [0,1]
x = Solution()
res = x.findMaxLength(a)
print(res)