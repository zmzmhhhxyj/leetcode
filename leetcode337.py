class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        self.memo = {}
        return self.helper(root)
    
    def helper(self,root):
        ans = 0
        if root in self.memo:
            return self.memo[root]
        if not root:
            return 0
        if root.left:
            ans += self.helper(root.left.left)+self.helper(root.left.right)
        if root.right:
            ans += self.helper(root.right.left)+self.helper(root.right.right)
        res = max(ans+root.val,self.helper(root.left)+self.helper(root.right))
        self.memo[root] = res
        return res

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

#a = [3,4,5,1,3,None,1]
a = [4,2,None,1,3]
tree = constructBinaryTree(a)
x = Solution()
res = x.rob(tree)
print(res)