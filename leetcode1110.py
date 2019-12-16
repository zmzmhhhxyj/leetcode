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
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        self.set_del = set(to_delete)
        root = self.remove(root)
        if root:
            self.ans.append(root)
        return self.ans

    def remove(self,root):
            if not root:return None
            root.left = self.remove(root.left)
            root.right = self.remove(root.right)
            #如果不用删root，直接返回该节点
            if root.val not in self.set_del:
                return root
            #root被删除的情况，把返回的左右直接加入ans
            if root.left:
                self.ans.append(root.left)
            if root.right:
                self.ans.append(root.right)
            #return None
        
tree = constructBinaryTree([1,2,3,4,5,6,7])        
solution = Solution()
x = solution.delNodes(tree,[3,5])
print(x)           
