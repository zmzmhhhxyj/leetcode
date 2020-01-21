from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":"abc","3":"def",'4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        self.dfs(mapping,digits,0,"",res)
        return res

    def dfs(self,mapping,digits,index,path,res):
        if len(digits)==len(path):
            res.append(path)
            return
        for i in range(index,len(digits)):
            for j in mapping[digits[i]]:
                self.dfs(mapping,digits,i+1,path+j,res)


x = Solution()
res = x.letterCombinations("23")
print(res)