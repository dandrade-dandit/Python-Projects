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

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node;

    def traverse_list(self):
        myStr = ""
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                # print(n.data, " ")
                myStr = myStr + str(n.data) + "->"
                n = n.next
        print(myStr[0:(len(myStr)-2)])

# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    ''' 
    Three nodes have been created. 
    We have references to these three blocks as head, 
    second and third 

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  | None |     | 2  | None |     |  3 | None | 
    +----+------+     +----+------+     +----+------+ 
    '''

    # llist.head.next = second;  # Link first node with second

    ''' 
    Now next of first Node refers to second.  So they 
    both are linked. 

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  | null |     |  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''

    # second.next = third;  # Link second node with the third node

    ''' 
    Now next of second Node refers to third.  So all three 
    nodes are linked. 

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''

    llist.insert_at_end(2)
    llist.insert_at_end(3)
    llist.insert_at_end(4)
    llist.insert_at_end(5)
    llist.insert_at_end(6)
    llist.insert_at_end(7)
    llist.insert_at_end(8)

    llist.traverse_list()