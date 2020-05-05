from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        i = 0
        while i<len(s):
            if dp[i]:
                for j in wordDict:
                    if s[i:i+len(j)]==j:
                        dp[i+len(j)] = True
            i+=1
        return dp[-1]


x = Solution()
a = x.wordBreak("aaaaaaa",["aaaa", "aaa"])
print(a)