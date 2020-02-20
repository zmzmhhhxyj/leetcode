from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generate(1,n) if n else []

    def generate(self,start,end):
        if start>end:
            return [None]
        res = []
        for i in range(start,end+1):
            res1 = self.generate(start,i-1)
            res2 = self.generate(i+1,end)
            for i in res1:
                for j in res2:
                    tmp = TreeNode(i)
                    tmp.left = i
                    tmp.right = j
                    res.append(tmp)
        return res

x = Solution()
a = x.generateTrees(5)
print(a)