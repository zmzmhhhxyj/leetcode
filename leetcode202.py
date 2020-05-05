class Solution:
    def isHappy(self, n: int) -> bool:
        numSet = set()
        while n not in numSet:
            numSet.add(n)
            n = sum([int(i)**2 for i in str(n)])
            if n==1:
                return True
        return False

x = Solution()
res = x.isHappy(19)
print(res)