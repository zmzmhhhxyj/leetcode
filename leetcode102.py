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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return 
        res,stack = [],[(root,0)]
        while stack:
            node,level = stack.pop(0)
            if len(res)<level+1:
                res.append([])
            res[level].append(node.val)
            if node.left:
                stack.append((node.left,level+1))
            if node.right:
                stack.append((node.right,level+1))
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        lcur,lnext = [],[]
        res = []
        lcur.append(root)
        level = 0
        while lcur:
            res.append([])
            while lcur:
                node = lcur.pop(0)
                if node.left:
                    lnext.append(node.left)
                if node.right:
                    lnext.append(node.right) 
                res[level].append(node.val)
            level+=1
            lcur = lnext
            lnext = []
        return res

    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root,res,0)
        return res
    def dfs(self,root,res,level):
        if not root:
            return 
        if len(res)<level+1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left,res,level+1)
        self.dfs(root.right,res,level+1)
        

tree = constructBinaryTree([3,9,20,None,None,15,7,None,None, None,None,7,9,2,5])
solution = Solution()
res = solution.levelOrder(tree)
print(res)  