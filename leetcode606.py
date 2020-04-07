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
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return
        s = str(t.val)
        l = self.tree2str(t.left)
        r = self.tree2str(t.right)

        if not t.left and not t.right:
            return s
        if not t.left:
            return s+"()"+"("+r+")"
        if not t.right:
            return s+"("+l+")"
        return s+"("+l+")"+"("+r+")"
        


tree = constructBinaryTree([3,9,20,None,None,15,7])
x=Solution()
res = x.tree2str(tree)
print(res)  