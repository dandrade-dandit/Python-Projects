# A simple Python program to introduce a linked list 
  
# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    # This function prints contents of linked list 
    # starting from head 
    def printList(self): 
        txt = ''
        temp = self.head 
        while (temp): 
            txt += str(temp.data) + ' => '
            temp = temp.next
        print(txt[:len(txt)-4])

        
# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 
    forth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)
    eigth = Node(8)
  
    llist.head.next = second; # Link first node with second  
    second.next = third; # Link second node with the third node 
    third.next = forth
    forth.next = fifth
    fifth.next = sixth
    sixth.next = seventh
    seventh.next = eigth

    llist.printList()