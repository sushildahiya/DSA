class BinaryTree:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

### Print Binary Tree
def printRecursive(root):
  if root == None:
    return
  print(root.data, end=" : ")
  if root.left != None:
    print("L", root.left.data, end=" ")
  if root.right != None:
    print("R", root.right.data)
  print()
  printRecursive(root.left)
  printRecursive(root.right)

### Take input of binary Tree
def inputBinaryTree():
  data = int(input())
  if data== -1:
    return 
  root = BinaryTree(data)
  root.left = inputBinaryTree()
  root.right = inputBinaryTree()
  return root

### Number of nodes in a binary tree
def nodesNoInBinaryTree(root):
  if root==None:
    return 0
  return 1 + nodesNoInBinaryTree(root.left)+nodesNoInBinaryTree(root.right)


  

root = inputBinaryTree()
printRecursive(root)
print(nodesNoInBinaryTree(root))