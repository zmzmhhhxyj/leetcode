from typing import List
from collections import deque
import collections
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
        if len(res)<level+1:
            res.append([])
        if cur:
            res[level].append(cur.val)
            queue.append([cur.left,level+1])
            queue.append([cur.right,level+1])
        if not cur:
            res[level].append("#")
    print(res)

class Solution:
        def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
            def serialize(root):
                if not root:
                    return "#"
                key = str(root.val) + "," + serialize(root.left) + "," + serialize(root.right)
                self.d[key]+=1
                if self.d[key] == 2:
                    self.ans.append(root.val)
                return key
            self.d = collections.defaultdict(int)
            self.ans = []
            serialize(root)
            return self.ans

  
x = Solution()
tree = constructBinaryTree([1,2,3,4,None,2,4,None,None,None,None,4])
# tree = constructBinaryTree([5])
ans = x.findDuplicateSubtrees(tree)
print(ans)
