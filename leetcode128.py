from typing import List
import collections
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        for i in nums:
            if i in d and d[i]!=0:
                continue
            if d[i-1]==0 and d[i+1]==0:
                d[i] = 1
            elif d[i-1]>0 and d[i+1]>0:
                l = d[i-1]
                r = d[i+1]
                d[i-l] = r+l+1
                d[i+r] = r+l+1
                d[i] = r+l+1
            elif d[i-1]>0:
                l = d[i-1]
                d[i-l],d[i]=l+1,l+1
            elif d[i+1]>0:
                l = d[i+1]
                d[i+l],d[i]=l+1,l+1
        return max(d.values()) if d.values() else 0

x = Solution()
# ans = x.longestConsecutive([1,2,3,6,5,4])
# ans = x.longestConsecutive([100, 4, 200, 1, 3, 2])
# ans = x.longestConsecutive([])
# ans = x.longestConsecutive([1,2,0,1])
ans = x.longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])
print(ans)