from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        stack.append(-1)
        heights.append(0)
        for i,height in enumerate(heights):
            while height<heights[stack[-1]] and stack[-1]>=0:
                left = stack.pop()
                maxarea = max(maxarea,(i-stack[-1]-1)*heights[left])
            stack.append(i)
        return maxarea
x = Solution()
res = x.largestRectangleArea([2,1,5,6,2,3])
print(res)