from typing import List
class Solution:
    def threeSum(self,nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                sum_3 = nums[i]+nums[l]+nums[r]
                if sum_3<0:
                    l=l+1
                if sum_3>0:
                    r=r-1
                if sum_3==0:
                    res.append((nums[i],nums[l],nums[r]))
                    while l<r and nums[l]==nums[l+1]:
                        l = l+1
                    while l<r and nums[r]==nums[r-1]:
                        r = r-1
                    l=l+1
                    r=r-1
        return res

x=Solution()
a=x.threeSum([-1, 0, 1, 2, -1, -4])
print(a)