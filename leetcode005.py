class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            tmp1 = self.helper(s,i,i)
            tmp2 = self.helper(s,i,i+1)
            if len(tmp1)>len(res):
                res = tmp1
            if len(tmp2)>len(res):
                res = tmp2
        return res


    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]

x = Solution()
res = x.longestPalindrome("babad")
print(res)