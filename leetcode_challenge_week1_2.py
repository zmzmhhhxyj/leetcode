class Solution:
    def isHappy(self, n: int) -> bool:
        sum_set = set()
        while n not in sum_set:
            sum_set.add(n)
            n = sum([int(num)**2 for num in str(n)])
            if n == 1:
                return True
        return False

x = Solution()
ans = x.isHappy(27)
print(ans)
