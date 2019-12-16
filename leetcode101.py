from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructBinaryTree(elemList):
    length = len(elemList)
    if(length == 0):
        return None
    _root = TreeNode(elemList[0])
    def recr(root, num):
        # num: number of node, start by 0 (root)
        leftNumber = 2*num+1
        rightNumber = 2*num+2
        if(leftNumber < length and elemList[leftNumber] != None):
            root.left = TreeNode(elemList[leftNumber])
            recr(root.left, leftNumber)
        else:
            root.left = None
        if(rightNumber < length and elemList[rightNumber] != None):
            root.right = TreeNode(elemList[rightNumber])
            recr(root.right, rightNumber)
        else:
            root.right = None
    recr(_root, 0)
    return _root

class Solution:
    def isSymmetric(self,root: TreeNode) -> bool:
        if not root:
            return True
        queue = deque([(root,root)])
        while queue:
            node1,node2 = queue.popleft()
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            elif node1.val!=node2.val:
                return False
            queue.append((node1.left,node2.right))
            queue.append((node1.right,node2.left))
        return True

tree = constructBinaryTree([[1,2,2,None,3,None,4]])
x = Solution()
a = x.isSymmetric(tree)
print(a)
        