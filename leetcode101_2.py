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
        def isSyn(l,r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return isSyn(l.left,r.right) and isSyn(l.right,r.left)
            return False
        return isSyn(root,root)

tree = constructBinaryTree([[1,2,2,3,4,4,3]])
x = Solution()
a = x.isSymmetric(tree)
print(a)
        