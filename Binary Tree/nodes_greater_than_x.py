### For a given a binary tree of integers and an integer X, find and return the total number of nodes of the given binary tree which are greater than X
class BinaryTree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def inputBinaryTree():
  data = int(input())
  if data == -1:
    return
  root = BinaryTree(data)
  root.left = inputBinaryTree()
  root.right = inputBinaryTree()
  return root


def printBinaryTree(root):
  if root == None:
    return
  print(root.data, end=": ")
  if root.left != None:
    print('L ', root.left.data, end=" ")
  if root.right != None:
    print('R ', root.right.data, end="")
  print()
  printBinaryTree(root.left)
  printBinaryTree(root.right)

### Count of nodes greater than x
def nodesGreaterThanX(root,x):
  if root==None:
    return 0
  nodesGreX=nodesGreaterThanX(root.left,x)
  nodesGreY=nodesGreaterThanX(root.right,x)
  if root.data>x:
    return 1+nodesGreY+nodesGreX
  return nodesGreY+nodesGreX


root=inputBinaryTree()
print(nodesGreaterThanX(root,6))