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
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root,float('-inf'),float('inf'))
        
    def helper(self,root,low,high):
        if not root:
            return True
        l = self.helper(root.left,low,root.val)
        r = self.helper(root.right,root.val,high)
        c = True
        if root.val<low or root.val>high:
            c = False
        return l and r and c


#x=constructBinaryTree([10,5,15,None,None,6,20])
x=constructBinaryTree([2,1,3])
solution = Solution()
a = solution.isValidBST(x)
print(a)