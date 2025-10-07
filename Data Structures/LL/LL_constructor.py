class Node:
    def __init__(self,value):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self,value):
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1

my_ll = LinkedList(5)
print('Head: ',my_ll.head.value)
print('Tail: ',my_ll.tail.value)
print('Length: ',my_ll.length)
        