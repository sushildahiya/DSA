### For a given binary tree of type integer,print all the nodes without any siblings.


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


def printNodesWithoutSibilings(root):
  if root == None:
    return
  printNodesWithoutSibilings(root.left)
  printNodesWithoutSibilings(root.right)
  if root.left != None and root.right == None:
    print(root.left.data, end=" ")
  elif root.left == None and root.right != None:
    print(root.right.data, end=" ")


root = inputBinaryTree()

printNodesWithoutSibilings(root)
