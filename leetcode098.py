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
    def isValidBST3(self, root: TreeNode) -> bool:
        output = []
        self.inorder(root,output)
        for i in range(1,len(output)):
            if output[i-1].val>=output[i].val:
                return False
        return True

    def inorder(self,root,output):
        if root == None:
            return
        self.inorder(root.left,output)
        output.append(root)
        self.inorder(root.right,output)

    def isValidBST2(self, root: TreeNode) -> bool:
        return self.helper(root,float('-inf'),float('inf'))
        
    def helper(self,root,low,high):
        if not root:
            return True
        l = self.helper(root.left,low,root.val)
        r = self.helper(root.right,root.val,high)
        if root.val<=low or root.val>=high:
            return False
        return l and r

    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        pre = -float("inf")
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val<=pre:
                return False
            pre = node.val
            root = node.right
        return True


x=constructBinaryTree([2,1,3])
solution = Solution()
a = solution.isValidBST(x)
print(a)