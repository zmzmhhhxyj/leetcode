class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tArray = {}
        sArray = {}
        minres = float("inf")
        res = ""
        count = 0
        for tc in t:
            tArray[tc] = tArray.get(tc,0)+1
        l = self.nextIdx(s,tArray,0)
        r = l
        if l==len(s):
            return ""
        while r<len(s):
            sArray[s[r]] = sArray.get(s[r],0)
            if sArray[s[r]]<tArray[s[r]]:
                count+=1
            sArray[s[r]]+=1
            while l<=r and count==len(t):
                if r-l+1<minres:
                    minres = r-l+1
                    res = s[l:r+1]
                if sArray[s[l]]<=tArray[s[l]]:
                    count-=1
                sArray[s[l]]-=1
                l = self.nextIdx(s,tArray,l+1)
            r = self.nextIdx(s,tArray,r+1)
        return res
     
    def nextIdx(self,s,tArray,start):
        for i in range(start,len(s)):
            if s[i] in tArray:
                return i
        return len(s)

x = Solution()
# res = x.minWindow("ADOBECODEBANC","ABC")
res = x.minWindow("cabwefgewcwaefgcf","cae")
print(res)