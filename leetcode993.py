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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xroot,xdepth = self.getPD(root,x,0)
        yroot,ydepth = self.getPD(root,y,0)
        if xroot!=yroot and xdepth==ydepth:
            return True
        else:
            return False
        
    def getPD(self,root,num,depth):
        if not root:
            return None,0
        if root.left:
            if root.left.val==num:
                return root,depth+1
            else:
                lroot,ldepth = self.getPD(root.left,num,depth+1)
                if lroot:
                    return lroot,ldepth
        if root.right:
            if root.right.val==num:
                return root,depth+1
            else:
                rroot,rdepth = self.getPD(root.right,num,depth+1)
                if rroot:
                    return rroot,rdepth
        return None,0

tree = constructBinaryTree([1,2,3,None,4,None,5])
# tree = constructBinaryTree([1,2,3,None,None,None,4,5])
x = Solution()
res = x.isCousins(tree,5,4)
# res = x.isCousins(tree,1,2)
print(res)