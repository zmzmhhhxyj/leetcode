from typing import List
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        count = 0
        left = False
        for l in shift:
            if l[0]==0:
                count -= l[1]
            else:
                count += l[1]
        if count<0:
            left=True
            count = -count
        move = count%len(s) 
        ans = ""
        if left:
            part = move
            ans+=s[part:]
            ans+=s[:part]
        else:
            part = len(s)-move
            ans += s[part:]
            ans += s[:part]
        return ans

s = "wpdhhcj"
b = [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]
x = Solution()
ans = x.stringShift(s,b)
print(ans)