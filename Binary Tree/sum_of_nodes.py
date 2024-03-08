class BinaryTree:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None


def inputBinaryTree():
  data=int(input())
  if data == -1:
    return 
  root=BinaryTree(data)
  root.left=inputBinaryTree()
  root.right=inputBinaryTree()
  return root

def printBinaryTree(root):
  if root ==None:
    return
  print(root.data,end=": ")
  if root.left !=None:
    print('L ',root.left.data,end=" ")
  if root.right !=None:
    print('R ',root.right.data,end="")
  print()
  printBinaryTree(root.left)
  printBinaryTree(root.right)


### Sum of nodes
def sumOfNodes(root):
  if root==None:
    return 0
  return root.data+sumOfNodes(root.left)+sumOfNodes(root.right)
root = inputBinaryTree()
printBinaryTree(root)
print(sumOfNodes(root))