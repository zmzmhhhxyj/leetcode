#using DFS
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p,q)]
        while stack:
            node1,node2 = stack.pop()
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            stack.append((node1.left,node2.left))
            stack.append((node1.right,node2.right))
        return True

x = Solution()
tree1 = constructBinaryTree([1,2,1])
tree2 = constructBinaryTree([1,2,3])
same = x.isSameTree(tree1,tree2)
print(same)