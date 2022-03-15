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
