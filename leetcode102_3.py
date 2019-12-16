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
        res, queue = [],deque([(root,0)])
        while queue:
            cur,level = queue.popleft()
            if cur:
                if len(res)<level+1:
                    res.append([])
                res[level].append(cur.val)
                queue.append([cur.left,level+1])
                queue.append([cur.right,level+1])
        return res

        

tree = constructBinaryTree([3,9,20,None,None,15,7,None,None, None,None,7,9,2,5])
solution = Solution()
res = solution.levelOrder(tree)
print(res)  