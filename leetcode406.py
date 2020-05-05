from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        # people_sort = sorted(people, key = lambda p: p[0],reverse=True)
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        people_dict = {}
        for p in people:
            people_dict.setdefault(p[0],[])
            people_dict[p[0]].append(p[1])
        # people_dict {4: [4], 5: [0, 2], 6: [1], 7: [0, 1]}
        hs = sorted(people_dict.keys(),reverse=True)
        # hs [7, 6, 5, 4]
        for h in hs:
            ks = sorted(people_dict[h])
            for k in ks:
                res.insert(k,[h,k])
        return res

x = Solution()
res = x.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
print(res)