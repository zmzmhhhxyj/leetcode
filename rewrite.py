class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.helper(root,{})
    
    def helper(self,root,memo):
        if not root:
            return 0 
        if root in memo:
            return memo[root]
        ans = 0
        if root.left:
            ans += self.helper(root.left.left,memo)+self.helper(root.left.right,memo)
        if root.right:
            ans += self.helper(root.right.left,memo)+self.helper(root.right.right,memo)
        res = max(root.val+ans,self.helper(root.left,memo)+self.helper(root.right,memo))
        memo[root] = res
        return res

def constructBinaryTree(elemList):
    length = len(elemList)
    if(length == 0):
        return None
    root = TreeNode(elemList[0])
    stack = [root]
    elemList.pop(0)
    while stack:
        node = stack.pop(0)
        if not elemList:
            break
        num2 = elemList.pop(0)
        l = TreeNode(num2)
        if num2!=None:
            stack.append(l)
            node.left = l
        if not elemList:
            break
        num3 = elemList.pop(0)
        r = TreeNode(num3)
        if num3!=None:
            stack.append(r)
            node.right = r
    return root

#a = [3,4,5,1,3,None,1]
a = [3,2,3,None,3,None,1]
tree = constructBinaryTree(a)
x = Solution()
res = x.rob(tree)
print(res)