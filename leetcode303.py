from  typing import List 
class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = nums
        for i in range(1,len(nums)):
            self.dp[i] = self.dp[i-1]+self.dp[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j]-(self.dp[i-1] if i>0 else 0)

x = NumArray([-2,0,3,-5,2,-1])
a = x.sumRange(0,5)
print(a)