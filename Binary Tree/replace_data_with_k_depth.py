### For a given Binary Tree of integers, replace each of its data with the depth of the tree.
### Root is depth 0 , hence the root is updated with 0. Replicate the same further going down the in the depth of the given tree.
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


def replaceKDepthNode(root):
  replaceKDepthHelper(root, 0)


def replaceKDepthHelper(root, count):
  if root == None:
    return

  replaceKDepthHelper(root.left, count + 1)
  replaceKDepthHelper(root.right, count + 1)
  root.data = count


root = inputBinaryTree()
printBinaryTree(replaceKDepthNode(root))
