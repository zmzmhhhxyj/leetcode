from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[''.join(sorted(s))].append(s)
        return ans.values()

x = Solution()
ans = x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(ans)