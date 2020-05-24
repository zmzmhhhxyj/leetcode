import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        myCounter = collections.Counter(s)
        res = []
        for k,v in sorted(myCounter.items(), key=lambda x: (x[1],x[0]),reverse=True):
            res+=[k]*v
        return "".join(res)

x = Solution()
ans = x.frequencySort("Aabb")
print(ans)