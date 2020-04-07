from typing import List
from collections import deque
import sys
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


class Solution:
    def averageOfLevels2(self, root: TreeNode) -> List[float]:
        stack = [(root,0)]
        count = [0]
        num = [0]
        res = []
        while stack:
            node,level = stack.pop(0)
            if level+1>len(num):
                count.append(0)
                num.append(0)
            count[level]+=node.val
            num[level]+=1
            if node.left:
                stack.append((node.left,level+1))
            if node.right:
                stack.append((node.right,level+1))
        for i in range(len(num)):
            res.append(count[i]/num[i])
        return res
    
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        lcur = [root]
        lnext = []
        count = 0
        num = 0
        res = []
        while lcur:
            for node in lcur:
                count+=node.val
                num+=1
                if node.left:
                    lnext.append(node.left)
                if node.right:
                    lnext.append(node.right)
            res.append(count/num)
            lcur = lnext
            lnext = []
            count,num = 0,0
        return res


tree = constructBinaryTree([3,9,20,6,2,15,7])
x=Solution()
res = x.averageOfLevels(tree)
print(res)