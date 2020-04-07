from typing import List
from collections import deque
import sys
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

def levelOrder(root: TreeNode) :
    res, queue = [],deque([(root,0)])
    while queue:
        cur,level = queue.popleft()
        if cur:
            if len(res)<level+1:
                res.append([])
            res[level].append(cur.val)
            queue.append([cur.left,level+1])
            queue.append([cur.right,level+1])
    print(res)


class Solution:
    def findSecondMinimumValuex(self, root: TreeNode) -> int:
        return self.dfs(root,root.val)
        
    def dfs(self,root,ans):
        if not root:
            return -1
        if ans<root.val: return root.val
        l = self.dfs(root.left,ans)
        r = self.dfs(root.right,ans)
        if l==-1:
            return r
        if r==-1:
            return l
        return min(l,r)
        

    def findSecondMinimumValuex2(self, root: TreeNode) -> int:
        stack = [root]
        min_2 = sys.maxsize
        found = False
        while stack:
            node = stack.pop(0)
            if node.val>root.val and node.val<min_2:
                min_2 = node.val
                found = True
                continue
            if node.left:
                stack.append((node.left))
            if node.right:
                stack.append((node.right))
        return min_2 if found else -1
            


tree = constructBinaryTree([2,2,5,None,None,5,7])
x=Solution()
res = x.findSecondMinimumValuex(tree)
print(res)