from typing import List

class Solution:
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

    def generateParenthesis2(self, n: int) -> List[str]:
        res = []
        self.back("",res,0,0,n)
        return res

    def back(self,path,res,l,r,n):
        if r == n:
            res.append(path)
            return
        if l<n:
            path += "("
            self.back(path,res,l+1,r,n)
            path = path[:-1]
        if r<l:
            path += ")"
            self.back(path,res,l,r+1,n)
            path = path[:-1]        

x = Solution()
ans = x.generateParenthesis(3)
print(ans)