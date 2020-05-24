from typing import List

class Solution:
    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        dp = [False]*(len(s)+1)
        dp[0] = True
        self.helper2(s,wordDict,0,res,"",dp)
        return res
    
    def helper2(self,s,wordDict,idx,res,path,dp):
        if idx==len(s) and dp[-1]==True:
            res.append(path)
            return
        if idx>len(s):
            return
        for word in wordDict:
            if s[idx:idx+len(word)]==word and dp[idx]==True:
                dp[idx+len(word)]=True
                if not path:
                    self.helper(s,wordDict,idx+len(word),res,path+word,dp)
                else:
                    self.helper(s,wordDict,idx+len(word),res,path+" "+word,dp)
                dp[idx+len(word)]=False

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s,wordDict,{})

    def helper(self,s,wordDict,memo):
        if s in memo:
            return memo[s]
        if not s:
            return
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(s)==len(word):
                res.append(word)
            else:
                restResult = self.helper(s[len(word):],wordDict,memo)
                for w in restResult:
                    w = word+ " "+w
                    res.append(w)
        memo[s] = res
        return memo[s]

x = Solution()
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
ans = x.wordBreak(s,wordDict)
print(ans)