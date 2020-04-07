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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        node = TreeNode(t1.val+t2.val)
        node.left = self.mergeTrees(t1.left,t2.left)
        node.right = self.mergeTrees(t1.right,t2.right)
        return node


a = [1,3,2,5]
b = [2,1,3,None,4,None,7]
t1 = constructBinaryTree(a)
t2 = constructBinaryTree(b)
x = Solution()
res = x.mergeTrees(t1,t2)
levelOrder(res)