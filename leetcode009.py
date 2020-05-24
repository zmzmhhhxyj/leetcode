class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev = 0
        tmp = x
        while tmp>0:
            last = tmp%10
            rev = rev*10+last
            tmp//=10
        return x==rev

x = Solution()
res = x.isPalindrome(112226)
print(res)