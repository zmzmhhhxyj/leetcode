from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generate(1,n)
    def generate(self,start,end):
        if start>end:
            return [None]
        res = []
        for i in range(start,end+1):
            root = TreeNode(i)
            lefts = self.generate(start,i-1)
            rights = self.generate(i+1,end)
            for left in lefts:
                for right in rights:
                    tmp = root
                    tmp.left = left
                    tmp.right = right
                    res.append(root)
        return res

x = Solution()
a = x.generateTrees(5)
print(a)