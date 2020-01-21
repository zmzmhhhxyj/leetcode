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
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight == rightHeight:
            return pow(2,leftHeight)+self.countNodes(root.right)
        else:
            return pow(2,rightHeight)+self.countNodes(root.left)

    def getHeight(self,root):
        if not root:
            return 0
        return 1 + self.getHeight(root.left)
            
tree = constructBinaryTree([1,2,3,4,5,6,7])
x = Solution()
res = x.countNodes(tree)
print(res)