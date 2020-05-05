# 200421
from  typing import List 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for num in nums:
            if not tail:
                tail.append(num)
                continue
            if num>tail[-1]:
                tail.append(num)
            else:
                idx = self.findidx(tail,num)
                if idx-1>=0 and tail[idx-1]==num:
                    continue
                tail[idx] = num
        return len(tail)
    
    def findidx(self,nums,num):
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<=num:
                l = mid+1
            else:
                r = mid
        return l


    def lengthOfLIS3(self, nums: List[int]) -> int:
        if nums is None: return None
        dp = [1]
        for i in range(1,len(nums)):
            max_num = 1
            for j in range(0,i):
                if nums[j]<nums[i] and dp[j]+1>max_num:
                    max_num = dp[j]+1
            dp.append(max_num)
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

x = Solution()
# a = x.lengthOfLIS([10,9,2,5,3,7,101,18])
a = x.lengthOfLIS([4,10,4,3,8,9])
print(a)