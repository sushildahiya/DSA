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

### Find the height of binary tree
def find_height(root):
  if root == None:
    return 0
  return 1 + max(find_height(root.right),find_height(root.left))

root = inputBinaryTree()
print(find_height(root))