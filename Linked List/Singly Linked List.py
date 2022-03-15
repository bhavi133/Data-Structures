Linked List : A linked list is a linear data structure that includes a series of connected nodes. Here, each node stores the data and the address of the next node.
  
# Step 1:
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

# Step 2:
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Step 3:
    def traverse(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="-->")
                n = n.ref
                
    # Step 4:
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # Step 5:
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # Step 6:
    def insert_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in a linked list!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
