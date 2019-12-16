import sys
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        tar_start = sys.maxsize
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                sum_3 = nums[i]+nums[l]+nums[r]
                diff = sum_3-target
                if diff<0:
                    l=l+1
                elif diff>0:
                    r=r-1
                elif diff==0:
                    return sum_3
                if abs(diff)<abs(tar_start-target):
                    tar_start = sum_3
        return tar_start

x=Solution()
a=x.threeSumClosest([-1,2,1,-4],1)
print(a)