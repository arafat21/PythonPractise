
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
        temp = Node(value)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp

LL = LinkedList(2)
LL.append(5)

print(LL.pop().value)
print(LL.pop().value)
print(LL.pop())
        