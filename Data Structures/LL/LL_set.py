class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_Node = Node(value)     
        self.head = new_Node
        self.tail = new_Node
        self.length = 1             
        
    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        self.length += 1
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False


LL = LinkedList(10)
LL.append(5)
LL.append(3)
LL.append(2)
LL.set(2, 100)
LL.printLL()
