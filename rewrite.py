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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res,stack = [],[(root,0)]
        while stack:
            node, level = stack.pop()
            if node:
                if len(res)<level+1:
                    res.append([])
                if level % 2==1:
                    res[level].append(node.val)
                else:
                    res[level].insert(0,(node.val))
                stack.append((node.left,level+1))
                stack.append((node.right,level+1))
        return res


        

tree = constructBinaryTree([3,9,20,None,None,15,7,None,None, None,None,7,9,2,5])
solution = Solution()
res = solution.zigzagLevelOrder(tree)
print(res)  