from typing import List
class Solution:
    def removeDuplicates(A: List[int]) -> int:
        if not A:
            return 0
        ii,jj = 1,1
        while jj<len(A):
            if A[ii-1]!=A[jj]:
                A[ii]=A[jj]
                ii = ii+1
            jj = jj+1
        return ii

x = Solution()
a = Solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(a)