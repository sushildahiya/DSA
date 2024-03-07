class Node:
  def __init__(self,data):
    self.data=data
    self.next = None

### Time complexity of taking input is O(N)
def takeInputEfficent():
  inputArr  = [int(ele) for ele in input().split(" ")]
  tail=None
  head=None
  for i in inputArr:
    if i==-1:
      break
    newNode = Node(i)
    if head is None:
      head=newNode
      tail=newNode
    else:
      tail.next=newNode
      tail=tail.next
  return head

def printLL(head):
  while head is not None:
    print(str(head.data)+" --->",end=" ")
    head=head.next
  print("None")

def count_nodes(head):
  count =0
  while head is not None:
    count+=1
    head=head.next
  return count

head = takeInputEfficent()
printLL(head)
print(count_nodes(head))