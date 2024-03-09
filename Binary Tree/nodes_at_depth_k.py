### Print the node at depth of k from root node
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


def printKDepthNode(root, k):
  printKDepthHelper(root, k, 0)


def printKDepthHelper(root, k, count):
  if root == None:
    return
  if count == k:
    print(root.data, end=" ")
    return
  printKDepthHelper(root.left, k, count + 1)
  printKDepthHelper(root.right, k, count + 1)


root = inputBinaryTree()
printKDepthNode(root, 2)
