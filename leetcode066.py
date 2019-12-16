from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1
        for i in range(len(digits)-1,0,-1):
            if digits[i]!=10:
                return digits
            digits[i] = 0
            digits[i-1] += 1
        if digits[0]==10:
            digits[0]=0
            return [1]+digits
        return digits

x = Solution()
a = x.plusOne([9,9,9])
print(a)