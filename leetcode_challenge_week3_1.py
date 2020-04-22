from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = len(nums)
        l1 = [1]*count
        l2 = [1]*count
        ans = [0]*count
        for i in range(1,count):
            l1[count-i-1] = l1[count-i]*nums[count-i]
            l2[i] = l2[i-1]*nums[i-1]
        for j in range(count):
            ans[j] = l1[j]*l2[j]
        return ans

x = Solution()
ans = x.productExceptSelf([])
print(ans)