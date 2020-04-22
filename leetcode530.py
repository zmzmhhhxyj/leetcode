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
        if len(res)<level+1:
            res.append([])
        if cur:
            res[level].append(cur.val)
            queue.append([cur.left,level+1])
            queue.append([cur.right,level+1])
        if not cur:
            res[level].append("#")
    print(res)

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev:
                self.ans = min(self.ans,abs(root.val-self.prev.val))
            self.prev = root
            inorder(root.right)
        self.ans = float("inf")
        self.prev = None
        inorder(root)
        return self.ans


    def getMinimumDifference2(self, root: TreeNode) -> int:
        return self.findDiff(root,float('-inf'),float('inf'))
        
    def findDiff(self,root,low,high):
        if not root:
            return high-low
        l = self.findDiff(root.left,low,root.val)
        r = self.findDiff(root.right,root.val,high)
        return min(l,r)

  
x = Solution()
tree = constructBinaryTree([5,3,9,None,4,7])
# tree = constructBinaryTree([5])
ans = x.getMinimumDifference(tree)
print(ans)
