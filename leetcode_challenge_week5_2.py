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
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not arr and not root:
            return True
        if not arr or not root:
            return False
        if arr[0]!=root.val: #not equal, no need to dfs
            return False
        if len(arr)==1 and (root.left or root.right):
            return False
        l = self.isValidSequence(root.left,arr[1:])
        r = self.isValidSequence(root.right,arr[1:])
        return l or r

# tree = constructBinaryTree([0,1,0,0,1,0,None,None,1,0,0])
# a = [0,1,1]
tree = constructBinaryTree([8,3,None,2,1,5,4])
a = [8]
x = Solution()
ans = x.isValidSequence(tree,a)
print(ans)
