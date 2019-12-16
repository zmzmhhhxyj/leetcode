import numpy as np
import random
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]
        dp.append(1)
        dp.append(2)
        dp.append(3)
        if n<3:
            return dp[n]
        for i in range(4,n+1):
            j=int(i**0.5)
            n_min = i
            for k in range(1,j+1):
                n_min = min(dp[i-k*k]+1,n_min)
            dp.append(n_min)
        return dp[-1]

    def numSquares1(self, n: int) -> int:
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
            dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        return dp[n]

x = Solution()
nums = np.random.randint(1,10000,10)
print(nums)
for i in range(10):
    a = x.numSquares1(nums[i])
    b = x.numSquares(nums[i])
    print(a,b)