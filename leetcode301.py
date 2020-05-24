from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l,r = 0,0
        res = []
        for i in s:
            if i=="(":
                l+=1
            elif i==")":
                if l>0:
                    l-=1
                else:
                    r+=1
        self.dfs(s,0,l,r,res)
        return res

    def isvalid(self,s):
        count = 0
        for i in s:
            if i==")":
                count-=1
            elif i=="(":
                count+=1
            if count<0:
                return False
        if count==0:
            return True
        else:
            return False
    
    def dfs(self,s,idx,l,r,res):
        if l==0 and r==0:
            if self.isvalid(s):
                res.append(s)
            return
        for i in range(idx,len(s)):
            if i>idx and s[i]==s[i-1]:
                continue
            if s[i]==")" and r>0:
                cur = s[:i]+s[i+1:]
                self.dfs(cur,i,l,r-1,res)
            elif s[i]=="(" and l>0:
                cur = s[:i]+s[i+1:]
                self.dfs(cur,i,l-1,r,res)
                
        
x = Solution()
# ans = x.removeInvalidParentheses("(a)())()")
ans = x.removeInvalidParentheses("()())()")
print(ans)