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


### Print binary tree in pre order traversal
def printPreOrder(root):
  if root == None:
    return
  print(root.data, end=" ")
  printPreOrder(root.left)
  printPreOrder(root.right)


### Print binary tree in-order traversal
def printInOrder(root):
  if root == None:
    return
  printInOrder(root.left)
  print(root.data, end=" ")
  printInOrder(root.right)


### Print binary tree post-order traversal
def printPostOrder(root):
  if root == None:
    return
  printPostOrder(root.left)
  printPostOrder(root.right)
  print(root.data, end=" ")


root = inputBinaryTree()
printPostOrder(root)
