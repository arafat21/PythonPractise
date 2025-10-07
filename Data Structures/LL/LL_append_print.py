class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self,value):
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1
    
    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
            self.length = 1
        else:
            self.tail.next = new_Node
            self.tail = new_Node
            self.length += 1
        
LL = LinkedList(7)
LL.append(9)
LL.append(11)

LL.printLL()
