### Remove leaf nodes of a tree
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

def removeLeaf(root):
  if root == None:
    return
  if root.left == None and root.right ==None:
    return None
  root.left=removeLeaf(root.left)
  root.right=removeLeaf(root.right)
  return root

root = inputBinaryTree()
printBinaryTree(root)