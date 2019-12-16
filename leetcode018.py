from typing import List
class Solution:
    def fourSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum2 = nums[i]+nums[j]
                if sum2 not in d:
                    d[sum2] = [(i,j)]
                else:
                    d[sum2].append((i,j))
        res = set()
        for key in d:
            sub = target-key
            if sub in d:
                list1 = d[key]
                list2 = d[sub]
                for (i,j) in list1:
                    for (x,y) in list2:
                        if i!=x and i!=y and j!=x and j!=y:
                            fourlist = [nums[i],nums[j],nums[x],nums[y]]
                            fourlist.sort()
                            res.add(tuple(fourlist))
        return list(res)


x = Solution()
a = Solution.fourSum([1, 0, -1, 0, -2, 2],0)
print(a)