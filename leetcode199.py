from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        list1 = self.rightSideView(root.right)
        list2 = self.rightSideView(root.left)
        return [root.val] + list1 + list2[len(list1):]

    def rightSideView2(self, root: TreeNode) -> List[int]:
        view = []
        def helper(node,depth):
            if not node:
                return
            if len(view)==depth:
                view.append(node.val)
            helper(node.right,depth+1)
            helper(node.left,depth+1)
        helper(root,0)
        return view

    def rightSideView3(self, root: TreeNode) -> List[int]:
        res,queue = [],[(root,1)]
        while queue:
            node, level = queue.pop()
            if node:
                if level>len(res):
                    res.append([])
                res[level-1].append(node.val)
                queue.append((node.right,level+1))
                queue.append((node.left,level+1))
        return [x[-1] for x in res]


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

tree = constructBinaryTree([7,3,15,1,None,9,20,None,2])
x = Solution()
res = x.rightSideView3(tree)
print(res)