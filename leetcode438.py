from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        winlen = len(p)
        windict = {}
        pdict = {}
        count = 0
        res = []
        for c in p:
            pdict[c] = pdict.get(c,0)+1
        # for i in range(len(s)-winlen+1):
        for i,c in enumerate(s):
            if count<winlen:
                windict[c] = windict.get(c,0)+1
                count += 1
            if count==winlen:
                if pdict==windict:
                    res.append(i-winlen+1)
                count-=1
                windict[s[i-winlen+1]]-=1
                if windict[s[i-winlen+1]]==0:
                    windict.pop(s[i-winlen+1])
        return res

x = Solution()
ans = x.findAnagrams("cbaebabacd","abc")
print(ans)