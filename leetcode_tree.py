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

# written by myself, no need to use extra "None" when parent is None
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

def levelOrder(root: TreeNode) :
    res, queue = [],deque([(root,0)])
    while queue:
        cur,level = queue.popleft()
        if cur:
            if len(res)<level+1:
                res.append([])
            res[level].append(cur.val)
            queue.append([cur.left,level+1])
            queue.append([cur.right,level+1])
    print(res)


tree = constructBinaryTree([3,9,20,None,None,15,7,None,None, None,None,7,9,2,5])
levelOrder(tree)
