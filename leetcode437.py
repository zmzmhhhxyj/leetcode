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
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        d = dict()
        d[0] = 1
        self.dfs(root,sum,d,0)
        return self.res
    
    def dfs(self,root,sum,d,curSum):
        if not root:
            return
        curSum += root.val
        rest = curSum - sum
        self.res += d.get(rest,0)
        d[curSum] = d.get(curSum,0)+1
        self.dfs(root.left,sum,d,curSum)
        self.dfs(root.right,sum,d,curSum)
        d[curSum]-=1

    def pathSum2(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.helper(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
        
    def helper(self,root,sum):
        count = 0
        if not root:
            return 0
        if sum==root.val:
            count+=1
        count += self.helper(root.left,sum-root.val)
        count += self.helper(root.right,sum-root.val)
        return count


tree = constructBinaryTree([10,5,-3,3,2,None,11,3,-2,None,1])
x = Solution()
ans = x.pathSum(tree,8)
print(ans)
