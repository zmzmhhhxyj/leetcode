from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        res = ""
        for i in l:
            if len(set(i))==1:
                res+=i[0]
            else:
                break
        return res


x = Solution()
res = x.longestCommonPrefix(["flower","flow","flight"])
print(res)