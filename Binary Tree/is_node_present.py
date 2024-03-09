### For a given Binary Tree of type integer and a number X, find whether a node exists in the tree with data X or not.

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

def isNode(root,x):
  if root == None:
    return False
  if root.data==x:
    return True
  return isNode(root.left,x) or isNode(root.right,x)

root= inputBinaryTree()
print(isNode(root,3))
