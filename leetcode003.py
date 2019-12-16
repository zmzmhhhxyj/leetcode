class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        max_len, start = 0,0
        for i,c in enumerate(s):
            if c in dict:
                max_len = max(max_len,i-start)
                start = max(start,dict[c]+1)
            dict[c]=i
        return max(max_len,len(s)-start)

x = Solution()
res = x.lengthOfLongestSubstring("dvdf")
print(res)