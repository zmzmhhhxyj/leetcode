import collections
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        i = 0
        res = []
        while i<len(nums):
        # 一开始 i<len(nums)-k+1.不对，i并非res长度
            while q and nums[i]>q[-1]:
                q.pop()
            if not q or nums[i]<=q[-1]:
            #第二次报错是 nums[i]<q[-1]。[-7,-8,7,5,7,1,6,0],4 错误
                q.append(nums[i])
            if i>=k-1:
                res.append(q[0])
                if nums[i-k+1]==q[0]:
                # 第一次写的是q的长度与k相同时pop，不对。[1,3,1,2,0,5],3错误
                    q.popleft()
            i+=1
        return res
        

x = Solution()
# res = x.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
# res = x.maxSlidingWindow([1,3,1,2,0,5],3)
res = x.maxSlidingWindow([-7,-8,7,5,7,1,6,0],4)
print(res)