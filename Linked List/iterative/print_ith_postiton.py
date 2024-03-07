class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


### Time complexity of taking input is O(N)
def takeInputEfficent():
  inputArr = [int(ele) for ele in input().split(" ")]
  tail = None
  head = None
  for i in inputArr:
    if i == -1:
      break
    newNode = Node(i)
    if head is None:
      head = newNode
      tail = newNode
    else:
      tail.next = newNode
      tail = tail.next
  return head


def printLL(head):
  while head is not None:
    print(str(head.data) + " --->", end=" ")
    head = head.next
  print("None")


### Time complexity O(M)
def print_ith_position(head, i):
  count = 0
  temp = head
  while temp is not None:
    if count == i:
      return temp.data
    count += 1
    temp = temp.next
  return


head = takeInputEfficent()
k = int(input())

printLL(head)
print(print_ith_position(head, k))
