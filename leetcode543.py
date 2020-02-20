class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return
        self.res = 0
        self.maxL(root)
        return self.res-1

    def maxL(self,node):
        if not node:
            return 0
        l = self.maxL(node.left)
        r = self.maxL(node.right)
        self.res = max(self.res,l+r+1)
        return max(l,r)+1


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

a = [1,2,NotImplemented,4,5,None,None,6,None,None,7]
tree = constructBinaryTree(a)
x = Solution()
res = x.diameterOfBinaryTree(tree)
print(res)