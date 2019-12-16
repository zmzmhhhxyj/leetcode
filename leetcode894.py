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
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N%2==0: return None
        if N==1:return [TreeNode(0)]
        ans = []
        for i in range(1,N,2):
            for l in self.allPossibleFBT(i):
                for r in self.allPossibleFBT(N-i-1):
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans

   
solution = Solution()
x = solution.allPossibleFBT(5)
print(x)   