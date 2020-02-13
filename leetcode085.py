from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxR = 0
        n = len(matrix[0])
        height = [0]*n
        #height[0]= int(matrix[0][0])
        stack = [-1]
        for row in matrix:
            for i in range(n):
                height[i] = height[i]+1 if row[i]=="1" else 0
            height.append(0)
            for i in range(n+1):
                while height[i]<height[stack[-1]] and stack[-1]>=0:
                    left_idx = stack.pop()
                    maxR = max(maxR,(i-stack[-1]-1)*height[left_idx])
                stack.append(i)
        return maxR

a = Solution()
res = a.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
])
print(res)