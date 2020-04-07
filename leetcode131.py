from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(s,path,res):
            if not s:
                res.append(path)
                return
            for i in range(1,len(s)+1):
                if self.isPalindrome(s[:i]):
                    dfs(s[i:],path+[s[:i]],res)
        dfs(s,[],res)
        return res

    def isPalindrome(self,s):
        if s==s[::-1]:
            return True
        else:
            return False
        
s = "aab"
x = Solution()
res = x.partition(s)
print(res)