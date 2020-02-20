from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        idx = len(nums)-k
        l,r = 0,len(nums)-1
        while l<=r:
            pivot = self.quickSelct(nums,l,r)
            if pivot>idx:
                r = pivot-1
            elif pivot<idx:
                l = pivot+1
            else:
                return nums[pivot]
        return -1

    def quickSelct(self,nums,l,r):
        i,j = l,l
        while j<r:
            if nums[j]>nums[r]:
                pass
            elif nums[j]<=nums[r]:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
            j+=1
        nums[i],nums[r] = nums[r],nums[i]
        return i

a = [3,2,3,1,2,4,5,5,6]
x = Solution()
res = x.findKthLargest([3,2,3,1,2,4,5,5,6],4)
print(res)