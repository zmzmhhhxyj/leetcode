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
    def recoverTree2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        lorder = []
        self.inorder(root,lorder)
        v1,v2 = self.findswap(lorder)
        self.changevalue(root,v1,v2)
        return

    def inorder(self,root,lorder):
        if not root:
            return
        self.inorder(root.left,lorder)
        lorder.append(root.val)
        self.inorder(root.right,lorder)
    
    def findswap(self,lorder):
        v1,v2 = lorder[0],lorder[0]
        changed = False
        for i in range(1,len(lorder)):
            if lorder[i]<lorder[i-1]:
                v1 = lorder[i]
                if changed==False:
                    v2 = lorder[i-1]
                    changed = True
                else:
                    continue
        return v1,v2

    def changevalue(self,root,v1,v2):
        if not root:
            return 
        if root.val == v1:
            root.val = v2
        elif root.val==v2:
            root.val = v1
        self.changevalue(root.left,v1,v2)
        self.changevalue(root.right,v1,v2)

    def recoverTree2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        lorder = []
        self.inorder(root,lorder)
        v1,v2 = self.findswap(lorder)
        self.changevalue(root,v1,v2)
        return

    def inorder(self,root,lorder):
        if not root:
            return
        self.inorder(root.left,lorder)
        lorder.append(root.val)
        self.inorder(root.right,lorder)
    
    def findswap(self,lorder):
        v1,v2 = lorder[0],lorder[0]
        changed = False
        for i in range(1,len(lorder)):
            if lorder[i]<lorder[i-1]:
                v1 = lorder[i]
                if changed==False:
                    v2 = lorder[i-1]
                    changed = True
                else:
                    continue
        return v1,v2

    def recoverTree(self, root: TreeNode) -> None:
        self.node1 = None
        self.node2 = None
        self.preNode = None
        self.inorder2(root)
        tmp = self.node1.val
        self.node1.val = self.node2.val
        self.node2.val = tmp
        return

    def inorder2(self,root):
        if not root:
            return
        self.inorder2(root.left)
        if self.preNode and self.preNode.val>root.val:
            self.node1 = root
            if not self.node2:
                self.node2 = self.preNode
        self.preNode = root
        self.inorder2(root.right)


tree = constructBinaryTree([3,1,4,None,None,2])
# tree = constructBinaryTree([1,3,None,None,2])
x = Solution()
ans = x.recoverTree(tree)
levelOrder(tree)
