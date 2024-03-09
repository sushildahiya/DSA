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

def leafNodesCount(root):
  if root==None:
    return 0
  if root.left == None and root.right==None:
    return 1
  return leafNodesCount(root.left)+leafNodesCount(root.right)

root= inputBinaryTree()
print(leafNodesCount(root))