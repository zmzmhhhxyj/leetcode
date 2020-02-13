class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp =[[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        dp[0][0] = True
        #if p starts with "*" 
        idx = 0
        while idx<len(p) and p[idx] == "*":
            dp[idx+1][0] = dp[idx][0]
            idx = idx+1

        for i in range(len(s)):
            for j in range(len(p)):
                if s[i]==p[j]:
                    dp[j+1][i+1] = dp[j][i]
                elif p[j]=="*":
                    dp[j+1][i+1] = dp[j][i] or dp[j][i+1] or dp[j+1][i]
                elif p[j] == "?":
                    dp[j+1][i+1] = dp[j][i]
        return dp[-1][-1]

x = Solution()
s = "aa"
p = "*"
res = x.isMatch(s,p)
print(res)