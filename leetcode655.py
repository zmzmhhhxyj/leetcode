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
    def printTree(self, root: TreeNode) -> List[List[str]]:
        height = self.getH(root)
        width =  2**height-1
        res = [[""]*width for i in range(height)]
        self.fill(root,res,0,width-1,0)
        return res
        
    def getH(self,root):
        if not root:
            return 0
        return max(self.getH(root.left),self.getH(root.right))+1
    
    def fill(self,root,res,l,r,level):
        if not root:
            return
        mid = (l+r)//2
        res[level][mid] = str(root.val)
        self.fill(root.left,res,l,mid,level+1)
        self.fill(root.right,res,mid+1,r,level+1)



tree = constructBinaryTree([3,9,20,None,None,15,7])
x=Solution()
res = x.printTree(tree)
print(res)  