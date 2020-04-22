# Definition for a binary tree node.
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

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        self.shelper(root,res)
        return ("#").join(map(str,res))
    
    def shelper(self,root,res):
        if not root:
            return
        res.append(root.val)
        self.shelper(root.left,res)
        self.shelper(root.right,res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        values = [int(value) for value in data.split('#')]
        # root = TreeNode(data[0])
        root = self.dhelper(values,float('-inf'),float('inf'))
        return root
        
    def dhelper(self,data,low,high):
        if len(data)>0 and data[0]>low and data[0]<high:
            root = TreeNode(data[0])     
            data.pop(0) 
            root.left = self.dhelper(data,low,root.val)
            root.right = self.dhelper(data,root.val,high)
            return root

root = constructBinaryTree([2,1,3])
codec = Codec()
# codec.deserialize(codec.serialize(root))
res = codec.deserialize(codec.serialize(root))
print(res)