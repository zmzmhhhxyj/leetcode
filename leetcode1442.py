class Solution:
    def maxScore(self, s: str) -> int:
        count0 = 0
        count1 = 0
        ans = float('-inf')
        for i in range(len(s)):
            if s[i]=='0':
                count0+=1
            else:
                count1+=1
            if i!=len(s)-1:
                ans = max(ans,count0-count1)
        return ans+count1
                

x = Solution()
# ans = x.maxScore("1111")
# ans = x.maxScore("010111")
# ans = x.maxScore("10111")
# ans = x.maxScore("00")
print(ans)