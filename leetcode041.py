from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            #每个i位置上放第i+1个正数
            #0<=nums[i]-1<len(nums) 如果该位置上数比0小或者超出长度范围，不算
            #nums[nums[i]-1]!=nums[i] 如果该位置上的数不是第i+1个数 nums[i]-1:该数应该去的位置
            while 0<=nums[i]-1<len(nums) and nums[nums[i]-1]!=nums[i]:
                tmp=nums[i]-1
                nums[i],nums[tmp]=nums[tmp],nums[i]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
            
x = Solution()
a = x.firstMissingPositive([7,8,9,11,12])
print(a)