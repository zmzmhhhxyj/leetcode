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

    def generate(self,first,last):
        if first > last:
            return [None]
        trees = []
        for root in range(first, last + 1):
            lefts = self.generate(first, root - 1)
            rights = self.generate(root + 1, last)
            for left in lefts:
                for right in rights:
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees.append(node)
        return trees

x = Solution()
a = x.generateTrees(5)
print(a)