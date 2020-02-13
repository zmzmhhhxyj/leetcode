class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0]*len(s)
        for i in range(1,len(s)):
            if s[i]==")":
                leftidx = i-dp[i-1]-1
                if s[i-1]=="(":
                    dp[i] = dp[i-2]+2
                elif leftidx>=0 and s[leftidx]=="(":
                    dp[i] = i-leftidx+1+dp[leftidx-1]    
        return max(dp)

a = "(()())"
x = Solution()
res = x.longestValidParentheses(a)
print(res)