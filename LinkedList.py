#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


#Linked List Class
class LinkedList:
    def __init__(self):
        self.head=None

    #insert node as head
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    #inser node at a given index
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if index == position:
            self.insertAtBegin(data)
        else:
            while (current_node != None and position+1 != index):
                position+=1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next= new_node
            else:
                print("index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
 
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
 
        current_node.next = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    def remove_first_node(self):
        if(self.head == None):
            return
 
        self.head = self.head.next

    def remove_last_node(self):
 
        if self.head is None:
            return
 
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
 
        current_node.next = None

    def remove_at_index(self, index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
        
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next


LL = LinkedList()
LL.insertAtBegin(1)
LL.printLL()
print("---------------------------")
LL.insertAtBegin(2)
LL.printLL()
print("---------------------------")
LL.insertAtIndex(3,1)
LL.printLL()
print("---------------------------")
LL.insertAtEnd(4)
LL.printLL()
print("---------------------------")

LL.remove_first_node()
LL.printLL()
print("---------------------------")
LL.remove_last_node()
LL.printLL()
print("---------------------------")
LL.remove_at_index(1)
LL.printLL()
print("---------------------------")

print(LL.sizeOfLL())
print("---------------------------")
LL.updateNode(5,0)
LL.printLL()
print("---------------------------")



