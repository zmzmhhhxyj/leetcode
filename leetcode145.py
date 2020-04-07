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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [],[root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root,res)
        return res
    
    def helper(self,root,res):
        if not root:
            return
        self.helper(root.left,res)
        self.helper(root.right,res)
        res.append(root.val)
            
tree = constructBinaryTree([3,9,20,None,None,15,7])
solution = Solution()
res = solution.postorderTraversal(tree)
print(res)  