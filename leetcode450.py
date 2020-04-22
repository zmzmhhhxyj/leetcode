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
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return
        if key>root.val:
            root.right = self.deleteNode(root.right,key)
            return root
        elif key<root.val:
            root.left = self.deleteNode(root.left,key)
            return root
        else: # delete root
            if not root.left and not root.right:
                return
            if not root.left and root.right:
                return root.right
            if not root.right and root.left:
                return root.left
            else:
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right,minNode.val)
                return root

    def findMin(self,root):
        while root.left:
            root = root.left
        return root


x = Solution()
# tree = constructBinaryTree([8,3,9,2,6,None,10,None,None,4,7])
# tree.left.right.left.right = TreeNode(5)
tree = constructBinaryTree([5,3,6,2,4,None,7])
ans = x.deleteNode(tree,3)
levelOrder(ans)
