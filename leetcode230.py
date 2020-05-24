from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# def constructBinaryTree(elemList):
#     length = len(elemList)
#     if(length == 0):
#         return None
#     _root = TreeNode(elemList[0])
#     def recr(root, num):
#         # num: number of node, start by 0 (root)
#         leftNumber = 2*num+1
#         rightNumber = 2*num+2
#         if(leftNumber < length and elemList[leftNumber] != None):
#             root.left = TreeNode(elemList[leftNumber])
#             recr(root.left, leftNumber)
#         else:
#             root.left = None
#         if(rightNumber < length and elemList[rightNumber] != None):
#             root.right = TreeNode(elemList[rightNumber])
#             recr(root.right, rightNumber)
#         else:
#             root.right = None
#     recr(_root, 0)
#     return _root

def constructBinaryTree(elemList):
    length = len(elemList)
    if(length == 0):
        return None
    root = TreeNode(elemList[0])
    stack = [root]
    elemList.pop(0)
    while stack:
        node = stack.pop(0)
        if not elemList:
            break
        num2 = elemList.pop(0)
        l = TreeNode(num2)
        if num2!=None:
            stack.append(l)
            node.left = l
        if not elemList:
            break
        num3 = elemList.pop(0)
        r = TreeNode(num3)
        if num3!=None:
            stack.append(r)
            node.right = r
    return root

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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            k-=1
            if k==0:
                return node.val
            root = node.right

    def kthSmallest3(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.res = 0
        self.inorder(root,k)
        return self.res

    def inorder(self,root,k):
        if not root:
            return
        self.inorder(root.left,k)
        self.count+=1
        if self.count == k:
            self.res = root.val
            return 
        self.inorder(root.right,k)

    def kthSmallest2(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)


l = [31,30,48,3,None,38,49,0,16,35,47,None,None,None,2,15,27,33,37,39,None,1,None,5,None,22,28,32,34,36,None,None,43,None,None,4,11,19,23,None,29,None,None,None,None,None,None,40,46,None,None,7,14,17,21,None,26,None,None,None,41,44,None,6,10,13,None,None,18,20,None,25,None,None,42,None,45,None,None,8,None,12,None,None,None,None,None,24,None,None,None,None,None,None,9]
# rep = [None if x==None else x for x in l]
# l = [5,3,6,2,4,None,None,1]
tree = constructBinaryTree(l)
x = Solution()
ans = x.kthSmallest(tree,1)
print(ans)
