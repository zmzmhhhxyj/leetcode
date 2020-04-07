from typing import List
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = dict()
        pre[0]=1
        n = len(nums)
        ans = 0
        sum_ = 0
        for i in range(n):
            sum_ += nums[i]
            left = sum_-k
            ans += pre.get(left,0)
            pre[sum_] = pre.get(sum_,0)+1
        return ans

    def subarraySum2(self, nums: List[int], k: int) -> int:
        presum = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            presum[i] = presum[i-1]+nums[i-1]
        ans = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if presum[j+1]-presum[i]==k:
                    ans+=1
        return ans
                    
x = Solution()
a = [1,1,-1,1]
res = x.subarraySum(a,1)
print(res)