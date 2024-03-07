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

def delete_node(head,pos):
  if head is None:
    return head
  if pos==0:
    return head.next
  count =0
  curr=head
  while count<pos-1 and curr is not None:
    curr=curr.next
    count+=1
  if curr is None or curr.next is None:
    return head
  curr.next=curr.next.next
  return head
  


head = takeInputEfficent()
printLL(head)
newHead  = delete_node(head,4)
printLL(newHead)
