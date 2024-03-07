### Create a linked list, take input from user as a list and convert it into a linked list, create print method to print linked list


class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


### Time Complexity of taking input is O(n^2)
def take_input():
  inputList = [int(ele) for ele in input().split(" ")]
  head = None
  for i in inputList:
    if i == -1:
      break
    newNode = Node(i)
    if head == None:
      head = newNode
    else:
      curr = head
      while curr.next is not None:
        curr = curr.next
      curr.next = newNode
  return head


def printLL(head):
  while head.next is not None:
    print(str(head.data), '-->', end=" ")
    head = head.next
  print("None")


head = take_input()
printLL(head)
