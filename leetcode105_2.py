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

def outputBinaryTreeByDot(root):
    # generate graphviz file
    if(root == None):
        print ("receive None input")
        exit()
    head = ["digraph G{\n"]
    nodeSector = ["\n"]
    edgeSector = ["\n"]
    tail = ["\n}"]
    def recr(root, num):
        _str = 'node{0}[label = "{1}"];\n'.format(num, root.val)
        nodeSector.append(_str)
        if(root.left != None):
            edgeSector.append("node{0} -> node{1};\n".format(num, 2*num+1))
            recr(root.left, 2*num+1)
        if(root.right != None):
            edgeSector.append("node{0} -> node{1};\n".format(num, 2*num+2))
            recr(root.right, 2*num+2)
    recr(root, 0)
    return "".join(head) + "".join(nodeSector) + "".join(edgeSector) + "".join(tail)

def showDotFile(_strDotFile, _fileName = None, _outputName = None):
    import os
    if(_fileName != None):
        fileName = _fileName
    else:
        fileName = "tempBinaryTreeFile.dot"
    if(_outputName != None):
        outputName = _outputName
    else:
        outputName = "tempBinaryTreeFile.pdf"
    ##  save .dot file
    with open(fileName, "w") as fileHandler:
        fileHandler.write(_strDotFile)
    path = os.getcwd()
    ## command to generate grapg with graphviz
    cmd = "dot {0}\{1} -Tpdf -o {0}\{2}".format(path, fileName, outputName)
    print(cmd)
    consoleHandler = os.popen(cmd)
    print(consoleHandler.read())
    ## open PDF file
    print(os.popen("{0}\{1}".format(path, outputName)).read())


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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return
        node = TreeNode(preorder[0])
        root = node
        idx = inorder.index(node.val)
        node.left = self.buildTree(preorder[1:idx+1],inorder[:idx])
        node.right = self.buildTree(preorder[idx+1:],inorder[idx+1:])
        return root

tree = constructBinaryTree([3,9,20,None,None,15,7,None,None, None,None,7,9,2,5])
solution = Solution()
root = solution.buildTree([3,9,10,20,15,7],[9,10,3,15,20,7])
levelOrder(root)
