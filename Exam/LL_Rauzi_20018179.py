class Node: 
    def __init__(self, cargo=None, next=None): 
        self.cargo = cargo 
        self.next  = next 
        
    def __str__(self):   
        return str(self.cargo)

class LinkedList: 

    def __init__(self): 
        self.length = 0 
        self.head   = None 

    def addFirst(self, cargo): 
        node = Node(cargo) 
        node.next = self.head 
        self.head = node 
        self.length = self.length + 1 
    
    def isEmpty(self):
        return self.head == None
    
    # generates a nicely formatted list 
    def printList(self):
        print('[', end = "")     
        temp = self.head
        while temp != None:
            if temp.next != None:
                print(str(temp) + ",", end = "")
            else:
                print(str(temp), end = "")
            temp = temp.next
        print(']')

    def removeFirst(self):
        if self.isEmpty(): #should use the method for this - better readability and consistency
            return None

        first_item = self.head
        self.head = self.head.next

        self.length -= 1

        return first_item.cargo #technically just first_item could be used here because the __str__ method returns cargo, however for use in potential functions this should be added

list1 = LinkedList()

list1.addFirst(7)
list1.addFirst(5)
list1.addFirst(3)
list1.addFirst(1)
list1.addFirst(1)
list1.addFirst(1)

list1.printList()

print(list1.removeFirst())

list1.printList()